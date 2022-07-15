"""plprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
import posts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.index, name='index'),
    path('base1/', posts.views.base1, name='base1'),
    path('base2/', posts.views.base2, name='base2'),
    path('notice/', posts.views.notice, name='notice'),
    path('find_id/', posts.views.find_id, name='find_id'),
    path('find_pw/', posts.views.find_pw, name='find_pw'),
    path('login/', posts.views.login, name='login'),
    path('register/', posts.views.register, name='register'),
    path('create/', posts.views.create, name='create'),
    path('donate/', posts.views.donate, name='donate'),
    path('donatesuc/', posts.views.donatesuc, name='donatesuc'),
    path('feedback/', posts.views.feedback, name='feedback'),
    path('feedbacksuc/', posts.views.feedbacksuc, name='feedbacksuc'),
    path('list/', posts.views.list, name='list'),
    path('read/', posts.views.read, name='read'),
    path('readreport/', posts.views.readreport, name='readreport'),
    path('update/', posts.views.update, name='update'),
    path('libr/', posts.views.like, name='like'),
    path('pay/', posts.views.pay, name='pay'),
    path('paysuc/', posts.views.paysuc, name='paysuc'),
    path('scrap/', posts.views.scrap, name='scrap'),
    path('difuser/', posts.views.difuser, name='difuser'),
    path('editprofile/', posts.views.editprofile, name='editprofile'),
    path('follower/', posts.views.follower, name='follower'),
    path('following/', posts.views.following, name='following'),
    path('mypage/', posts.views.mypage, name='mypage'),
    path('plumusing/', posts.views.plumusing, name='plumusing'),
    path('setting/', posts.views.setting, name='setting'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)