
from xml.etree.ElementInclude import include   
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
import posts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.index, name='index'),
    path('base', posts.views.base, name='bas'),
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
    #####################################################
    path('post/',include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)