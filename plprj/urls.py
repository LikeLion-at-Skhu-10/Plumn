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
from django.urls import path, include
#계층적으로 이루어진 url을 앱을 이용해 효율적으로 관리하려면 include를 쓰면 됨
#accounts, mypage 앱 폴더 안에 인위적으로 urls.py 작성했음
#원래의 urls.py엔 include 작성
import posts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.index, name='index'),
    #이런 url 이름 하에 생기는 모든 url들은 각각의 앱 폴더.urls.py라고 하는 파이썬 파일에서 관리함
    path('', include('posts.urls')),
    path('', include('accounts.urls')),
    path('', include('mypage.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)