import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordContextMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from accounts.models import User
from posts.models import Post
from .models import Profile, Follow, Notification
from .forms import EditprofileForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views import View

# 마이페이지
@login_required(login_url='/login/')
def mypage(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    
    # 마이페이지 내 나의 정보
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()
    
    #팔로우 상태?
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()
    
    context={
        'profile':profile,
        'following_count':following_count,
        'followers_count':followers_count,
        'posts_count':posts_count,
        'follow_status':follow_status,}
    return render(request, 'mypage.html', context)
    
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()


#프로필 수정 - 확인
@login_required(login_url='/login/')
def edit_profile(request):
    user = request.user.id #로그인 auth를 안써서.. 확인해야 할 듯.
    profile = Profile.objects.get(userid=user)
    if request.method == 'POST' :
        form = EditprofileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save(commit=False)
            if Profile.objects.filter(username=form.cleaned_data['username']) :#수정하려는 닉네임이 있다면
                form = EditprofileForm
                error_message = "이미 존재하는 이름입니다."
                return render(request, 'editprofile.html', {'form':form, "error_message":error_message})
            else:
                user.username = form.cleaned_data['username']
                user.save()
            return redirect('mypage')
    else:
        form = EditprofileForm()
        return render(request, 'editprofile.html', {'form':form})
        
#비밀번호 변경 - 확인
@login_required(login_url='/login/')
def password_edit(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 성공적으로 변경했습니다.")
            return redirect('mypage') #패스워드 변경 완료로 바꿔도 무방
    else:
        password_change_form = PasswordChangeForm(request.user)
        
    return render(request, 'mypage/password_change.html', {'password_change_form':password_change_form})


#알람 확인 - 확인
def show_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date') #내림차순 정렬
    Notification.objects.filter(user=user, has_seen=False).update(has_seen=True) #알람 확인시 has_seen true
    
    context = {'notifications':notifications}
    
    return render(request, 'notifications.html', context)

# 알람 삭제 - 확인
def delete_notification(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete()
    return redirect('notifications')

# 알람 몇 개 왔는지 - 확인
def count_notifications(request):
    count_notifications = 0
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(user=request.user, has_seen=False).count()
        
    return {'count_notifications':count_notifications}
 