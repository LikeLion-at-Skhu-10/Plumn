from turtle import back
from django import forms
from distutils.command.clean import clean
from typing_extensions import Required
from .models import Profile
from accounts.models import User
from argon2 import PasswordHasher
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class EditprofileForm(forms.Form):
    username = forms.CharField(
        required= True,
        widget=forms.TextInput(
        attrs={'class' : 'input_margin', 'placeholder' : '닉네임 입력' }),
        error_messages={
            'required' : '닉네임을 입력해주세요.',
            'unique' : '이미 존재하는 닉네임입니다.'}
    )  

    userintro = forms.CharField(
        max_length=256,
        required = False,
        widget=forms.TextInput(
        attrs={'class' : 'input_margin', 'placeholder' : '소개말' }),
    )
    
    userphoto = forms.ImageField(required=False)
    background_colors = forms.ChoiceField()
    
    class Meta:
        model = Profile
        fields = ['username', 'userintro', 'userphoto','background_colors']
        
    def clean(self):
        cleaned_data = super().clean()
        
        username = cleaned_data.get('username')
        userintro = cleaned_data.get('userintro')
        userphoto = cleaned_data.get('userphoto')
        background_colors = cleaned_data.get('background_colors')
        
        if username:
            new_username = Profile.objects.get(username=username)
            if Profile.objects.filter(new_username=self.cleaned_data['username']).exists():
                return self.add_error('new_username', '이미 존재하는 닉네임입니다.')
            else:
                self.username = new_username
                self.userintro = userintro
                self.userphoto = userphoto
                self.background_colors = background_colors


REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
class PasswordChangeForm(forms.Form):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class' : 'input_margin', 'placeholder' : '비밀번호 입력'}),
        error_messages={'required' : '비밀번호를 입력해 주세요.'}
    )
    
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class' : 'input_margin', 'placeholder' : '비밀번호 확인'}),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )
    
    class Meta:
        model = User
        fields = ['password']
    
        # --- django built-in validator
    def clean_password(self):
        new_password1 = self.cleaned_data['new_password1']
        validate_password(new_password1)
        return new_password1

    # --- check duplicate
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['new_password2'] != cd['new_password2']:
            raise forms.ValidationError('패스워드가 일치하지 않습니다.')
        return cd['new_password2']

