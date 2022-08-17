from distutils.command.upload import upload
from pdb import post_mortem
from pyexpat import model
from django.db import models
import posts

from posts.views import setting

#post class 제목과 글/ 글 생성 시간/ 이미지/ 좋아요/유저
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(posts.User, on_delete=models.CASCADE, null=False)
    like_users = models.ManyToManyField(models.settings.AUTH_USER_MODEL, related_name='like_articles')
    user = models.ForeignKey(posts.User, on_delete=models.CASCADE, null=False)

def __str__(self):
    return self.title

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to = 'images/', blank= True, null = True)

class Comment (models.Model):
    article = models.ForeignKey(models.Article, on_delete=models.CASCADE)
    user = models.ForeignKey(models.settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
        
#피드백 창으로, 제목과 내용, 피드백한 시간을 알려줌 
class Feedback(models.Model):
    title = models.CharField(max_length=100)
    Comment = models.TextField()
    Cre_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
        
    
    