from dataclasses import field
from django import forms
from posts.views import Comment
from .models import Post, Article


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        field = ['title', 'body','image']

## 댓글 생성 forms임. 
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article', 'user',)

