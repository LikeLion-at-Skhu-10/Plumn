from time import time
from django.shortcuts import render, redirect, get_object_or_404 #get_list_or_404
from .models import Post, Likes
from accounts.models import User
from mypage.models import Profile, Follow
from .forms import FeedbackForm, ObjectionForm, PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
############################################################
@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post_date = timezone.now()
            form.save()
            return redirect('list')
    else:
        form = PostForm()
        return render(request, 'blog/create.html', {'form':form})

def list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts':posts})

def read(request, id):
    post = get_object_or_404(Post, id=id)
    profile = Profile.objects.filter(user_posts_id_id=id)
    recommendation = Post.objects.all() #post 테이블의 모든 객체 불러오서 recommendation변수에 저장.  
    return render(request, 'blog/read.html', {'post':post, 'profile':profile, 'recommendation':recommendation})

############################################################
def index(request):
    user = request.user
    if user.is_authenticated:
        user = User.objects.get(id=user.id)
        profile = Profile.objects.get(id=user.id)
        posts_count = Post.objects.filter(user=user).count()
        following_count = Follow.objects.filter(follower=user).count()
        followers_count = Follow.objects.filter(following=user).count()

        context={
            'profile':profile,
            'following_count':following_count,
            'followers_count':followers_count,
            'posts_count':posts_count,
            }
        return render(request, 'index.html', context)
    return render(request, 'index.html')

def base(request):
    user = request.user
    if user.is_authenticated:
        user = User.objects.get(id=user.id)
        profile = Profile.objects.get(id=user.id)
        posts_count = Post.objects.filter(user=user).count()
        following_count = Follow.objects.filter(follower=user).count()
        followers_count = Follow.objects.filter(following=user).count()

        context={
            'profile':profile,
            'following_count':following_count,
            'followers_count':followers_count,
            'posts_count':posts_count,
            }
        return render(request, 'base.html', context)
    return render(request, 'base.html')

def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return render(request, 'blog/read.html', {'form':form, 'post':post})
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/update.html', {'form':form, 'post':post})

def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('list')

def notice(request):
    return render(request, 'notice.html')

def scrap(request):
    return render(request, 'libr/scrap.html')

def like(request):
    return render(request, 'libr/like.html')

def donate(request):
    return render(request, 'blog/donate.html')

def pay(request):
    return render(request, 'libr/pay.html')

# 피드백
@login_required(login_url='/login/')
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.obj_date = timezone.now()
            form.save()
            form.save_m2m()
            return render(request, 'blog/feedbacksuc.html', {'form':form})
        
    else:
        form = FeedbackForm ()
        return render(request, 'blog/feedback.html', {'form':form})

# 이의제기
@login_required(login_url='/login/')
def readreport(request):
    objection_form = ObjectionForm()
    post = get_object_or_404(Post, id=id)
    context = {'form' : objection_form, 'post':post}
    if request.method == 'POST':
        form = ObjectionForm(request.POST)
        print(form)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.obj_date = timezone.now()
            form.save()
            return redirect('read', post.id) # 원래 기존 글 페이지로 돌아감
    else:
        return render(request, 'blog/readreport.html', context)

'''
# 추천
@login_required(login_url='/login/')
def like(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	current_likes = post.likes
	liked = Likes.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		like.save()
		current_likes = current_likes + 1

	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes = current_likes - 1

	post.likes = current_likes
	post.save()

	return redirect('details', args=[post_id])

@login_required
def favorite(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	profile = Profile.objects.get(user=user)

	if profile.favorites.filter(id=post_id).exists():
		profile.favorites.remove(post)

	else:
		profile.favorites.add(post)

	return redirect('details', args=[post_id])

def scrap(request):
    return render(request, 'libr/scrap.html')

def like(request):
    return render(request, 'libr/like.html')
'''

# 댓글 생성과 삭제 코드이나, forms, urls 연결되지 않아 주석 처리함.
#def comments_create(request, pk):
    #if request.user.is_authenticated:
        #article = get_object_or_404(Article, pk=pk)
        #comment_form = CommentForm(request.POST)
        #if comment_form.is_valid():
            #comment = comment_form.save(commit=False)
            # comment.article = article
            # comment.user = request.user
    #         # comment.save()
    #     return redirect('articles:detail', article.pk)
    # return redirect('accounts:login')

# def comments_delete(request, article_pk, comment_pk):
#     if request.user.is_authenticated:
#         comment = get_object_or_404(Comment, pk=comment_pk)
#         if request.user == comment.user:
#             comment.delete()
#     return redirect('articles:detail', article_pk)