# Generated by Django 4.0.6 on 2022-10-28 18:16

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
