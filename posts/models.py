from distutils.command.upload import upload
from pdb import post_mortem
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from accounts.models import User
from mypage.models import Notification
from django.db.models.signals import post_save, post_delete

#from posts.views import setting

#post class 제목과 글/ 글 생성 시간/ 이미지/ 추천 / 유저
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=False)
    content = models.TextField(null=False) # 내용 부분 도대체 어떻게 처리해야 할지?
    post_date = models.DateTimeField(auto_now_add=True) 
    background_image = models.ImageField(upload_to='images/', blank=True) #제목 배경 사진
    like_users = models.ManyToManyField(User, related_name='like_articles') #추천수
    topic = models.ManyToManyField('Topic') #토픽
    
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

#class Photo(models.Model):
#    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#    image = models.ImageField(upload_to = 'images/', blank= True, null = True)

# 댓글
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True) # create 했을 때
    updated = models.DateTimeField(auto_now=True) # 수정하고 저장 시에 
    
    def user_comment_post(sender, instance, *args, **kwargs): # 댓글 알람 
        comment = instance
        post = comment.post
        text_preview = comment.body[:90]
        sender = comment.user
        notify = Notification(post=post, sender=sender, user=post.user, text_preview=text_preview ,notification_type=2)
        notify.save()

    def user_del_comment_post(sender, instance, *args, **kwargs): # 유저가 댓글 삭제 시
        like = instance
        post = like.post
        sender = like.user

        notify = Notification.objects.filter(post=post, sender=sender, notification_type=2)
        notify.delete()
    
    def __str__(self):
        return self.content

post_save.connect(Comment.user_comment_post, sender=Comment)
post_delete.connect(Comment.user_del_comment_post, sender=Comment)
        
#피드백  
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) #유저가 탈퇴해도 피드백은 남아있음.
    feedback = models.TextField() 
    feed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
        
#이의제기
class Objection(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) #이하동문
    objection = models.TextField()
    obj_date = models.DateTimeField(auto_now_add=True)
    OBJ_CHOICES = (
        ('FALSE_FACT', '허위 사실 유포'), ('ILLEGAL', '불법 정보 유포'),
        ('LEAK', '개인 정보 유출'), ('DUPLICATION', '도배 및 중복 글')
    )
    obj_choices = models.CharField(max_length=100, choices=OBJ_CHOICES)
    
    def __str__(self):
        return self.obj_choices
    
#추천
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

    def user_liked_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user
        notify = Notification(post=post, sender=sender, user=post.user, notification_type=1)
        notify.save()

    def user_unlike_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user

        notify = Notification.objects.filter(post=post, sender=sender, notification_type=1)
        notify.delete()
#스크랩
