from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile

class EditprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'userintro', 'userphoto']
'''
class PasswordChangeForm(PasswordChangeForm):
    # clean_new_password2 재정의 시에는 super()함수 호출이 필요하다. (부모에 존재하는 유효성 검사이다.)
    def clean_new_password1(self):
        # new_password1에 대한 유효성 검사를 추가로 정의한다.
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.super().cleaned_data.get('new_password2')
        if old_password and new_password1:
            if old_password == new_password1:  # 기존 암호와 같을 경우 폼 에러를 일으킨다.
                raise forms.ValidationError('새로운 암호는 기존 암호와 다르게 입력해주세요')
        return new_password1
'''