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
    path('/', include('posts.urls')),
    path('', include('accounts.urls')),
    path('', include('mypage.urls')),
    path('')
]


# #######
# # app_name = 'articles'
# urlpatterns = [
# 	# ...생략...
    
#     path('<int:pk>/comments/', views.comments_create, name='comments_create'),
#     path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
# ]  -- class Comment에 대한 urls 임. 어디다가 써야할지 몰라 여기에 적음.