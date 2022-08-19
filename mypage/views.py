from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
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
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.hashers import check_password
from django.template.defaulttags import register

# 마이페이지
# @login_required(login_url='/login/')
def mypage(request):
    user = request.user
    profile = Profile.objects.get(id=user.id)
    
    # 마이페이지 내 나의 정보
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    followers = Follow.objects.filter(following=user)
    follower_list = {}
    for follower in followers:
        follower_profile = Profile.objects.filter(id=follower.follower_id)
        follower_list[id] = follower_profile
        
    
    followings = Follow.objects.filter(follower=user)
    following_list = {}
    for following in followings:
        following_profile = Profile.objects.filter(id=following.following_id)
        following_list[id] = following_profile
    context={
        'profile':profile,
        'following_count':following_count,
        'followers_count':followers_count,
        'posts_count':posts_count,
        'follower_list':follower_list,
        'followeing_list':following_list,
        }
    
    return render(request, 'mypage.html', context)

# difuser    
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(userid=user)
    posts = Post.objects.filter(user=user).order_by('post_date')
    
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    # 구독자 / 관심 작가
    followers = Follow.objects.filter(following=user)
    follower_list = {}
    for follower in followers:
        follower_profile = Profile.objects.filter(id=follower.follower_id)
        follower_list[id] = follower_profile
        
    
    followings = Follow.objects.filter(follower=user)
    following_list = {}
    for following in followings:
        following_profile = Profile.objects.filter(id=following.following_id)
        following_list[id] = following_profile
    # 구독 상태
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

	#Pagination
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    
    context = {
		'posts_paginator': posts_paginator,
        'posts' : posts,
		'profile':profile,
		'following_count':following_count,
		'followers_count':followers_count,
		'posts_count':posts_count,
		'follow_status':follow_status,
        'follower_list':follower_list,
        'followeing_list':following_list,
        
	}

    return render(request, 'difuser.html', context)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


#프로필 수정 - 확인
@login_required(login_url='/login/')
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(id=user.id)
    form = EditprofileForm()

    if request.method == 'POST' :
        form = EditprofileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.username = form.cleaned_data.get('username')
            profile.userintro = form.cleaned_data.get('userintro')
            profile.userphoto = form.cleaned_data.get('userphoto')
            profile.save()
            return redirect('mypage')
        # form 이 유효했을때와 안 유효했을때와의 둘다 케이스를 넣어줘야
        # 그래야 유효하지 않는 form 이 들어오더라도 Http response object 를 받을 수 있다
        else:
            messages.info(request, form.error_messages)
            return render(request, 'editprofile.html', {'form':form , 'profile': profile})
    else:
        return render(request, 'editprofile.html', {'form':form, 'profile': profile})
        
#비밀번호 변경 - 확인
@login_required(login_url='/login')
def setting(request):
    user = request.user
    profile = Profile.objects.get(id=user.id)

    form = PasswordChangeForm()
    context = {'form':form}
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            new_password1 = form.cleaned_data.get('new_password1')
            user.set_password(new_password1)
            update_session_auth_hash(request, user)
            user.save()
            return redirect('mypage') 
        else:
            context['form'] = form
            if form.errors:
                for value in form.errors.values():
                    context['error'] = value
        return render(request, 'setting.html', context)
    else:
        return render(request, 'setting.html', context)

#팔로우
@login_required(login_url='/login/')
def follow(request, username, option):
    following = get_object_or_404(User, username=username)
    
    try:
        f, created = Follow.objects.get_or_create(follower=request.user, following=following)

        if int(option) == 0:
            f.delete()
			
        else:
            posts = Post.objects.all().filter(user=following)[:25]
    
        return HttpResponseRedirect(reverse('profile', args=[username]))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile', args=[username]))

'''
def followers(request, username):
    follower = Follow.objects.filter(follower=username)
    context = follower
    return render(request, 'follower.html', context)

def followings(request, username):
    followings = Follow.objects.filter(following=username)
    context = followings
    return render(request, 'following.html', context)
'''
#알람 확인 - 확인
def show_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date') #내림차순 정렬
    Notification.objects.filter(user=user, has_seen=False).update(has_seen=True) #알람 확인시 has_seen true
    
    context = {'notifications':notifications}
    
    return render(request, 'notice.html', context)

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
 