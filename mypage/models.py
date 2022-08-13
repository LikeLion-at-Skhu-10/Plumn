from django.db import models
from accounts.models import User
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from PIL import Image
from django.conf import settings
import os

def user_directory_path(instance, filename):
    # 사진파일 MEDIA_ROOT/user_<id>/<filename>에 업로드 되게 설정
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name

#프로필
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    userintro = models.CharField(max_length=256, verbose_name='유저 소개말')
    user_posts_id = models.ForeignKey(to='posts.Post', on_delete=models.CASCADE, related_name='user_post')  #reltaed_name은 역참조
    scrap = models.ManyToManyField(to='posts.Post') #
    userphoto= models.ImageField(upload_to='images/', blank=True, null=True) #유저 이미지, 디폴트 이미지와 upload_to 설정
    #여기서 프로필 사진 설정 해야 할듯
    
    color1= "CEC8D2"
    color2 = "FFF5EB"
    color3 = "FFE0D1"
    color4 = "C7D8EB"
    color5 = "E5DECD"
    
    COLORS = (
        (color1, "color1"), (color2, "color2"), (color3, "color3"), (color4, "color4"), (color5, "color5")
    )
    background_colors = models.CharField(max_length=6, choices=COLORS, default=color1)
    
    def __str__(self):
        return self.userid
 
#decorater를 통해서 signal에 필요한 인자들을 넘겨준다 
#그리고 만약 User 모델에 새로운 record가 추가되면 Profile 모델의 user 필드를 instance의 값을 넣어주어 Profile에 새로운 record를 생성하라는 코드   
@receiver(post_save, sender=User)
def creat_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)

#관심작가 및 구독자
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='follower')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='following')

    #구독 알람
    def user_follow(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        following = follow.following
        notify = Notification(sender=sender, user=following, notification_type=3)
        notify.save()
        
    #구독해제 알람
    def user_unfollow(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        following = follow.following

        notify = Notification.objects.filter(sender=sender, user=following, notification_type=3)
        notify.delete()
  
#알람
class Notification(models.Model):
    # 1 = 추천, 2 = 댓글, 3 = 팔로우, 4 = 새 게시글
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'), (4, 'Post'))
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    
    user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(User, related_name='nofitication_from', on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(to='posts.Post', on_delete=models.CASCADE, related_name='noti_post', blank=True, null=True)
    text_preview = models.CharField(max_length = 90, blank=True)
    date = models.DateTimeField(default=timezone.now)
    has_seen = models.BooleanField(default=False) #봤는지 확인


#Follow
post_save.connect(Follow.user_follow, sender=Follow)
post_delete.connect(Follow.user_unfollow, sender=Follow)