from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def notice(request):
    return render(request, 'notice.html')
    
def find_id(request):
    return render(request, 'accounts/find_id.html')

def find_pw(request):
    return render(request, 'accounts/find_pw.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

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