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
]