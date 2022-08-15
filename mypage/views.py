import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
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
def mypage(request):
    user = request.user
    profile = Profile.objects.get(id=user.id)
    
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

# difuser    
def profile(request):
    user = request.user
    profile = Profile.objects.get(id=user.id)
    posts = Post.objects.filter(user=user).order_by('-posted')
    
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    # 구독 상태
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

	#Pagination
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    
    context = {
		'posts': posts_paginator,
		'profile':profile,
		'following_count':following_count,
		'followers_count':followers_count,
		'posts_count':posts_count,
		'follow_status':follow_status,
	}

    return render(request, 'profile.html', context)


#프로필 수정 - 확인
@login_required(login_url='/login/')
def edit_profile(request):
    user = request.user
    #profile = Profile.objects.get(id=user.id)
    
    if request.method == 'POST' :
        form = EditprofileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('mypage')
    else:
        form = EditprofileForm()
        return render(request, 'editprofile.html', {'form':form})
        
#비밀번호 변경 - 확인
@login_required(login_url='/login')
def password_edit(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            new_password1 = form.cleaned_data.get('new_password1')
            user.set_password(new_password1)
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 성공적으로 변경했습니다.")
            return redirect('mypage') 
        else:
            form = PasswordChangeForm(instance=user)
    else:
        return render(request, 'password_change.html', {'form':form})

#팔로우(임시)
@login_required(login_url='/login')
def follow(request, username, option):
    following = get_object_or_404(User, username=username)

    try:
        f, created = Follow.objects.get_or_create(follower=request.user, following=following)

        if int(option) == 0:
            f.delete()
			
        else:
            posts = Post.objects.all().filter(user=following)[:25]

        return render(request, 'profile.html', args=[username])
    except User.DoesNotExist:
        return render(request, 'profile', args=[username])


def followers(request, username):
    follower = Follow.objects.filter(follower=username)
    context = follower
    return render(request, 'follower.html', context)

def followings(request, username):
    followings = Follow.objects.filter(following=username)
    context = followings
    return render(request, 'following.html', context)
    
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
 