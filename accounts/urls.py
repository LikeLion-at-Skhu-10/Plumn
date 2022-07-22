from django.urls import path
from accounts import views

urlpatterns=[
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    #path('findid/', views.findid, name='findid'),
    #path('findpw/', views.findpw, name='findpw'),
]