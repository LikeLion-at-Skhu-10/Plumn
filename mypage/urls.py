from django.urls import path
from mypage import views
from .views import PasswordChangeView #LoginRequiredMixin

urlpatterns=[
    path('mypage/', views.mypage, name='mypage'),
    path('editprofile/', views.edit_profile, name='editprofile'),
    #path('passwordchange/', views.PasswordChangeView.as_view(), name='passwordchange'),
    path('notificaitons/', views.show_notifications, name='notifications'),
    path('<noti_id>/delete/', views.delete_notification, name='delete-notifications'),
    path('<username>/', views.profile, name='profile'),
    path('setting/', views.password_edit, name='setting'),
    path('followers/', views.followers, name='followers'),
    path('followings/', views.followings, name='followings'),
]