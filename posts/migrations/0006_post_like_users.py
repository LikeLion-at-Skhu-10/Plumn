# Generated by Django 4.0.6 on 2022-11-05 21:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_alter_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
