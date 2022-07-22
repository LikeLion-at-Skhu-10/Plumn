import json, time, random, requests

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from argon2 import PasswordHasher
from accounts.forms import RegisterForm
from django.views import View
from django.http import JsonResponse
from .models import Authentication
from .utils import make_signature, access_key, secret_key, send_phone_number, uri, API_URL

# Create your views here.
def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pw)
        
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def register(request):
    register_form = RegisterForm()
    context = {'forms' : register_form}
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User(
                user_id = register_form.user_id,
                user_pw = register_form.user_pw,
                user_name = register_form.user_name,
                user_phone = register_form.user_phone
            )
            user.save()
            return redirect('login/')
        else:
            context['forms'] = register_form
            if register_form.erors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'accounts/register.html', context)
    
    else:
        return render(request, 'accounts/register.html', context)

def logout(request):
    auth.logout(request)
    return redirect('main')

# 네이버 SMS 인증
class SmsSendView(View):
    def send_sms(self, phone_number, auth_number):
        timestamp = str(int(time.time() * 1000))  
        headers = {
            'Content-Type': "application/json; charset=UTF-8", # 네이버 참고서 차용
            'x-ncp-apigw-timestamp': timestamp, # 네이버 API 서버와 5분이상 시간차이 발생시 오류
            'x-ncp-iam-access-key': access_key, #(예시 = 'nCH86JcJ6FCl40eYc4qp')
            'x-ncp-apigw-signature-v2': make_signature(timestamp) # utils.py 이용
        }
        body = {
            "type": "SMS", 
            "contentType": "COMM",
            "from": send_phone_number, # 사전에 등록해놓은 발신용 번호 입력, 타 번호 입력시 오류
            "content": f"[인증번호:{auth_number}]", # 메세지 형식
            "messages": [{"to": f"{phone_number}"}] # 네이버 양식에 따른 messages.to 입력
        }
        body = json.dumps(body)
        requests.post(API_URL, headers=headers, data=body)
        
    def post(self, request):
        data = json.loads(request.body)
        try:
            input_mobile_num = data['phone_number']
            auth_num = random.randint(1000, 10000) # 랜덤숫자 생성, 4자리로 계획하였다.
            auth_mobile = Authentication.objects.get(phone_number=input_mobile_num)
            auth_mobile.auth_number = auth_num
            auth_mobile.save()
            self.send_sms(phone_number=data['phone_number'], auth_number=auth_num)
            return JsonResponse({'message': '인증번호 발송완료'}, status=200)
        except Authentication.DoesNotExist: # 인증요청번호 미 존재 시 DB 입력 로직 작성
            Authentication.objects.create(
                phone_number=input_mobile_num,
                auth_number=auth_num,
            ).save()
            self.send_sms(phone_number=input_mobile_num, auth_number=auth_num)
            return JsonResponse({'message': '인증번호 발송 및 DB 입력완료'}, status=200)

# 네이버 SMS 인증번호 검증
class SMSVerificationView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            verification = Authentication.objects.get(phone_number=data['phone_number'])

            if verification.auth_number == data['auth_number']:
                return JsonResponse({'message': '인증 완료되었습니다.'}, status=200)

            else:
                return JsonResponse({'message': '인증 실패입니다.'}, status=400)

        except Authentication.DoesNotExist:
            return JsonResponse({'message': '해당 휴대폰 번호가 존재하지 않습니다.'}, status=400)