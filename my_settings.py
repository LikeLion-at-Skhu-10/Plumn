#장고에 MySQL연동시켜 데베 세팅 툴파일 생성한 것.
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'plumn', # db이름
        'USER': 'root', # 로그인-유저 명
        'PASSWORD': 'unprecedented1',# 로그인- 비밀번호
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}