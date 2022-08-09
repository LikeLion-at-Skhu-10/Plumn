from distutils.command.upload import upload
from pdb import post_mortem
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from accounts.models import User
from posts.views import setting

#post class 제목과 글/ 글 생성 시간/ 이미지/ 좋아요/유저
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    #image = models.ForeignKey(on_delete=models.CASCADE, null=False)
    like_users = models.ManyToManyField(User, related_name='like_articles')

    def __str__(self):
        return self.title

#토픽
class Topic(models.Model):
    TOPIC_CHOICES = (
        ('LIFE', '가정 / 생활'), ('HEALTH', '건강'), ('ECONOMY / MANAGEMENT', '경제 / 경영'), 
        ('LANGUAGE', '국어 / 외국어'), ('COMPUTER / IT', '컴퓨터 / IT'), ('POLITICS / SOCIETY', '정치 / 사회'),
        ('LITERATURE', '문학'), ('CHILD', '유아 / 아동'), ('TRAVEL', '여행'), 
        ('HISTORY', '역사'), ('ART', '예술'), ('HUMANITIES', '인문'),
        ('PEOPLE', '인물'), ('SELF-IMPROVEMENT', '자기계발'), ('SCIENCE', '과학'), ('RELIGION', '종교'),
        ('COOK', '요리'), ('CULTURE', '문화'), ('ENGINEERING', '공학')
    )
        
    topic = models.CharField(max_length = 50, choices=TOPIC_CHOICES, default=None)


class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to = 'images/', blank= True, null = True)

# 댓글
class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True) # create 했을 때
    updated = models.DateTimeField(auto_now=True) # 수정하고 저장 시에 

    def __str__(self):
        return self.content
        
#피드백  
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True) #유저가 탈퇴해도 피드백은 남아있음.
    feedback = models.TextField() 
    feed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
        
#이의제기
class Objection(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True) #이하동문
    objection = models.TextField()
    obj_date = models.DateTimeField(auto_now_add=True)
    OBJ_CHOICES = (
        ('FALSE_FACT', '허위 사실 유포'), ('ILLEGAL', '불법 정보 유포'),
        ('LEAK', '개인 정보 유출'), ('DUPLICATION', '도배 및 중복 글')
    )
    obj_choices = models.CharField(max_length=100, choices=OBJ_CHOICES)
    
    def __str__(self):
        return self.obj_choices