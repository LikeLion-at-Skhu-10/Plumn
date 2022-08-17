from time import time
from django.shortcuts import render, redirect, get_object_or_404 #get_list_or_404
import posts
from .models import Post, Likes
from mypage.models import Profile
from .forms import FeedbackForm, ObjectionForm #PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def notice(request):
    return render(request, 'notice.html')
    
def create(request):
    return render(request, 'blog/create.html')

def donate(request):
    return render(request, 'blog/donate.html')

def donatesuc(request):
    return render(request, 'blog/donatesuc.html')

def feedback(request):
    return render(request, 'blog/feedback.html')

def feedbacksuc(request):
    return render(request, 'blog/feedbacksuc.html')

def list(request):
    return render(request, 'blog/list.html')

def read(request):
    return render(request, 'blog/read.html')

def readreport(request):
    return render(request, 'blog/readreport.html')

def update(request):
    return render(request, 'blog/update.html')

def like(request):
    return render(request, 'libr/like.html')

def pay(request):
    return render(request, 'libr/pay.html')

def paysuc(request):
    return render(request, 'libr/paysuc.html')

def scrap(request):
    return render(request, 'libr/scrap.html')

def difuser(request):
    return render(request, 'mypage/difuser.html')

def editprofile(request):
    return render(request, 'mypage/editprofile.html')

def follower(request):
    return render(request, 'mypage/follower.html')

def following(request):
    return render(request, 'mypage/following.html')

def mypage(request):
    return render(request, 'mypage/mypage.html')

def plumusing(request):
    return render(request, 'mypage/plumusing.html')

def setting(request):
    return render(request, 'mypage/setting.html')

def notice(request):
    return render(request, 'notice.html')

'''
##############################
@login_required #로그인 시 가능하게끔
def post(request):
    if request.method == 'POST' :
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.user = request.user
        post.save()
        #name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다.
        for img in request.FILES.getlist('imgs'):
            #Photo 객체를 하나 생성한다.
            photo=Photo()
            #외래키로 현재 생성한 Post의 기본키를 참조
            photo.post = post
            #imgs로부터 가져온 이미지 파일 하나를 저장한다
            photo.image = img
            #데이터베이스에 저장
            photo.save()
            ###################### #1:urls 와 #2:html 설정해야함.
        return redirect('#1' + str(post.id))
    else:
        return render(request, '#2')
##################### #1 안에 html 넣어야 함
def read(request):
    posts = Post.objects
    return render(request, '#1', {'posts':posts})

############### #1 url입력   #2 html입력하기 
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            form.save_m2m()
            return redirect('#1')
    else:
        form = PostForm(instance=post)
        return render(request, '#2', {'form':form})

# 글 삭제
def delete(request, id) :
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('readlist')

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
'''
# 피드백
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
    context = {'form' : objection_form}
    if request.method == 'POST':
        form = ObjectionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.obj_date = timezone.now()
            form.save()
            form.save_m2m()
            return redirect('read') # 원래 기존 글 페이지로 돌아감
    else:
        return render(request, 'blog/readreport.html', context)

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
