from django.urls import path
from mypage import views
from .views import PasswordChangeView #LoginRequiredMixin
import posts.views as post_views

urlpatterns=[
    path('mypage/', views.mypage, name='mypage'),
    path('editprofile/', views.edit_profile, name='editprofile'), # 프로필 변경
    path('setting/', views.setting, name='setting'), #비밀번호 변경
    #path('passwordchange/', views.PasswordChangeView.as_view(), name='passwordchange'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/follow/<option>', views.follow, name='follow'),
    path('notificaitons/', views.show_notifications, name='notifications'),
    path('<noti_id>/delete/', views.delete_notification, name='delete-notifications'),
    path('scraps/', views.scraps, name='scraps'),
    path('likes/', views.likes, name='likes'),
    path('window/', post_views.window, name='window'),
    path('fail/', post_views.fail, name='fail'),
    path('success/', post_views.success, name='success'),
    #path('followers/<int:id>', views.followers, name='followers'),
    #path('followings/<int:id>', views.followings, name='followings'),
]