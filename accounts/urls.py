from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('logout/', views.logout, name='logout'),
    path('findid/', views.findid, name='find_id'), 
        
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"), #비밀번호 초기화
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]