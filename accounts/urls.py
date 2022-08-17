from django.urls import path
from accounts import views
from posts import views as posts_views

urlpatterns=[
    path('base/', posts_views.base, name='base'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('find_id/', views.findid, name='find_id'), 
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"), 
    path('password_reset/', views.PasswordResetView.as_view(), name="find_pw"), #비밀번호 초기화. 'find_pw'로 했더니 안돼서 이걸로 바꿈.
    path('password_reset_done/', views.PasswordResetDoneView.as_view(), name="password_reset_address"),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #path('admin/', admin.site.urls),
    path('', posts_views.index, name='index'),
    path('notice/', posts_views.notice, name='notice'),
    path('create/', posts_views.create, name='create'),
    path('donate/', posts_views.donate, name='donate'),
    path('donatesuc/', posts_views.donatesuc, name='donatesuc'),
    path('feedback/', posts_views.feedback, name='feedback'),
    path('feedbacksuc/', posts_views.feedbacksuc, name='feedbacksuc'),
    path('list/', posts_views.list, name='list'),
    path('read/', posts_views.read, name='read'),
    path('readreport/', posts_views.readreport, name='readreport'),
    path('update/', posts_views.update, name='update'),
    path('libr/', posts_views.like, name='like'),
    path('pay/', posts_views.pay, name='pay'),
    path('paysuc/', posts_views.paysuc, name='paysuc'),
    path('scrap/', posts_views.scrap, name='scrap'),
    path('difuser/', posts_views.difuser, name='difuser'),
    path('editprofile/', posts_views.editprofile, name='editprofile'),
    path('follower/', posts_views.follower, name='follower'),
    path('following/', posts_views.following, name='following'),
    path('mypage/', posts_views.mypage, name='mypage'),
    path('plumusing/', posts_views.plumusing, name='plumusing'),
    path('setting/', posts_views.setting, name='setting'),
]