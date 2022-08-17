from django.urls import path
from posts import views 
from accounts import views as account_views
urlpatterns=[
    path('base/', views.base, name='base'),
    path('notice/', views.notice, name='notice'),
    
    #path('create/', views.create, name='create'),
    #path('list/', views.list, name='list'),
    #path('read/', views.read, name='read'),
    #path('update/', views.update, name='update'),
    
    path('feedback/', views.feedback, name='feedback'), #피드백
    path('readreport/<int:id>', views.readreport, name='readreport'), # 이의제기
]