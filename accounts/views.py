import json, requests, time, random
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.views.generic import TemplateView, FormView
#from argon2 import PasswordHasher
from django.views import View
from django.http import JsonResponse
from .models import User#, Authentication
from django.template import RequestContext
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordContextMixin
# 이메일 가입을 위한 SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if User.objects.filter(email=email).exists():
            if user is not None:
                auth.login(request, user)
                return redirect('find_id')
            else:
                messages.info(request, "비밀번호를 다시 입력해주세요.")
                return render(request, 'login.html')
        else:
            messages.info(request, "해당 아이디는 존재하지 않습니다.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('main')

#회원가입
#에러 메세지(이메일, 닉네임, 전화번호)만 추가하면 됨 -> 폼으로 그냥 하자
def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirm']:
            email = request.POST.get('email') 
            #request.POST['']로 html에서 input 값 name을 각각 변수로 지정
            password = request.POST['password']
            password_confirm = request.POST['password_confirm']
            username = request.POST.get('user_name', False)
            userphone = request.POST['user_phone']
                    
            user = User.objects.create_user(email=email, password=password, username=username, user_phone=userphone)

            user.save()
            user.is_active = False # 유저 비활성화
            #user.save()
            current_site = get_current_site(request) 
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST['email']
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return redirect("login")
        else:
            messages.info(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'register.html')
    return render(request, 'register.html')
            
# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("login")
    else:
        return render(request, 'login.html', {'error' : '계정 활성화 오류'})
         
         
#아이디 찾기
def findid(request):
    if request.method == 'POST' :
        find_id = request.POST['user_phone']
        user = User.objects.filter(user_phone=find_id)
        if user is not None:
            return render(request, 'find_id_success.html', {'user':user}) 
        else:
            messages.info(request, "해당 전화번호는 없습니다.")
            return render(request, 'find_id.html')
    else:
        return render(request, 'find_id.html')
          
def find_id_succeess(request):
    return render(request, 'find_id_success.html')

#비밀번호 초기화하기 위해 아이디(=이메일) 존재하는 여부 검색
class PasswordResetView(PasswordResetView):
    template_name = "find_pw.html" #템플릿 변경하려면 다음과 같은 형식으로 입력
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exist():
            return super().form_valid(form)
        else:
            messages.info("해당하는 이메일이 존재하지 않습니다.")
            return render(self.request, 'find_pw.html')

#초기화하려는 아이디계정 이메일 존재하면, 초기화 이메일 성공 템플릿
class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = ""
    title = ("Password reset sent")
    
#비밀번호 초기화
class PasswordResetConfirmView(PasswordContextMixin, FormView):
    template_name = "find_pw_success.html"
    success_url = reverse_lazy("password_reset_complete")
    
#초기화 성공    
class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = ""
    title = ("Password reset complete")