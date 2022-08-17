from dataclasses import field
from django import forms
#from .views import Comment, objection
from .models import Post, Feedback, Objection


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image'] #추천 / 스크랩은 별개?
        labels = {
            'title' : '제목',
            'content' : '내용',
        }
## 댓글 생성 forms임. 
#class CommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#        fields = '__all__'
        
# 피드백
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback']
        
# 이의제기
class ObjectionForm(forms.ModelForm):
    class Meta:
        model = Objection
        fields = ['objection', 'obj_choices']