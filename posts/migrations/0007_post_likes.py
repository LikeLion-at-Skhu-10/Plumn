# Generated by Django 4.0.6 on 2022-11-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_topic_alter_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
