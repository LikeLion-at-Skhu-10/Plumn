# Generated by Django 4.0.6 on 2022-08-12 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('LIFE', '가정 / 생활'), ('HEALTH', '건강'), ('ECONOMY / MANAGEMENT', '경제 / 경영'), ('LANGUAGE', '국어 / 외국어'), ('COMPUTER / IT', '컴퓨터 / IT'), ('POLITICS / SOCIETY', '정치 / 사회'), ('LITERATURE', '문학'), ('CHILD', '유아 / 아동'), ('TRAVEL', '여행'), ('HISTORY', '역사'), ('ART', '예술'), ('HUMANITIES', '인문'), ('PEOPLE', '인물'), ('SELF-IMPROVEMENT', '자기계발'), ('SCIENCE', '과학'), ('RELIGION', '종교'), ('COOK', '요리'), ('CULTURE', '문화'), ('ENGINEERING', '공학')], default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('background_image', models.ImageField(blank=True, upload_to='images/')),
                ('like_users', models.ManyToManyField(related_name='like_articles', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ManyToManyField(to='posts.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Objection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objection', models.TextField()),
                ('obj_date', models.DateTimeField(auto_now_add=True)),
                ('obj_choices', models.CharField(choices=[('FALSE_FACT', '허위 사실 유포'), ('ILLEGAL', '불법 정보 유포'), ('LEAK', '개인 정보 유출'), ('DUPLICATION', '도배 및 중복 글')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like', to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feed_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
