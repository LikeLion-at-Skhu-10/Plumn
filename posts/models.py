from pyexpat import model
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    cre_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

def __str__(self):
    return self.title
    
class Comment(models.Model):
    def __str__(self):
        return self.text

    blog_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.CharField(max_length=500)

class Feedback(models.Model):
    title = models.CharField(max_length=100)
    Comment = models.TextField()
    Cre_Date = models.DateTimeField(auto_now_add=True)
    
    