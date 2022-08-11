from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.utils import timezone
#from django.utils.translation import ugettext_lazy
from random import randint
from django.core.validators import RegexValidator #전화번호 입력을 위한 유효성검사
 
# verbose_name : admin페이지에서 보일 컬럼명
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='유저 아이디') 
    password = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    username = models.CharField(max_length=32, unique=True, primary_key=True, verbose_name='유저 이름')
    phoneNumRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    user_phone = models.CharField(validators = [phoneNumRegex], max_length=11, unique=True, verbose_name='유저 전화번호')
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=False)
    date_joined = models.DateTimeField('가입일', default=timezone.now)
    #    last_login = models.DateTimeField('마지막 로그인시간', default=timezone.now)
    objects = UserManager()
    
    
    USERNAME_FIELD = 'email'                                        # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['username', 'user_phone']                   # 필수입력값
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user' #테이블 이름
        verbose_name = '유저' 
        verbose_name_plural = '유저'
        swappable = 'AUTH_USER_MODEL'
        
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
