from django.db import models
from django.core.validators import RegexValidator #전화번호 입력을 위한 유효성검사
 
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')
    user_pwd = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=32, unique=True, verbose_name='유저 이름')
    phoneNumRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    user_phone = models.CharField(validators = [phoneNumRegex], max_length=11, unique=True, verbose_name='유저 전화번호')
    #OneToOneField.. 어떻게 할지 생각해볼것
    
    def __str__(self):
        return self.user_name
    
    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'