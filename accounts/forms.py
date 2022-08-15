from distutils.command.clean import clean
from typing_extensions import Required
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from .models import User
from django.core.exceptions import ValidationError
from django.forms.widgets import ClearableFileInput
from argon2 import PasswordHasher
from django.contrib.auth import password_validation
#from django.contrib.auth.password_validation import password_validators_help_text_html

#회원가입 폼
class RegisterForm(forms.Form):
    username = forms.CharField(
        required= True,
        widget=forms.TextInput(
        attrs={'class' : 'input_margin', 'placeholder' : '닉네임 입력' }),
        error_messages={
            'required' : '닉네임을 입력해주세요.',
            'unique' : '이미 존재하는 닉네임입니다.'}
    )   
     
    email = forms.EmailField(
        required = True,
        widget=forms.EmailInput(
            attrs={'class' : 'input_margin', 'placeholder' : '이메일 아이디 입력'}),
            error_messages={
            'required' : '아이디를 입력해 주세요.',
            'unique' : '이미 존재하는 이메일 계정입니다.'}
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class' : 'input_margin', 'placeholder' : '비밀번호 입력' }),
        error_messages={'required' : '비밀번호를 입력해 주세요.'}
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class' : 'input_margin', 'placeholder' : '비밀번호 확인'}),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )

    user_phone = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={'class' : 'input_margin', 'placeholder' : '전화번호 입력'}),
            error_messages={
            'required' : '올바른 전화번호를 입력해 주세요.',
            'unique' : '이미 존재하는 전화번호 입니다.'}
    )    
        
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'user_phone',
        ]

    def clean(self):
        cleaned_data = super().clean()
        
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        user_phone = cleaned_data.get('user_phone')
        
        if password != password_confirm:
            return self.add_error('password_confirm', '비밀번호가 다릅니다.')
        elif not (2 <= len(username) <= 8):
            return self.add_error('username', '이름은 2~8자로 입력해 주세요.')
        elif 8 > len(password):
            return self.add_error('password', '비밀번호는 8자 이상으로 적어주세요.')
        elif User.objects.filter(username=self.cleaned_data['username']).exists():
            return self.add_error('username', '이미 존재하는 이름입니다.')
        elif User.objects.filter(email=self.cleaned_data['email']).exists():
            return self.add_error('email', '이미 존재하는 이메일입니다.')
        elif User.objects.filter(user_phone=self.cleaned_data['user_phone']).exists():
            return self.add_error('user_phone', '이미 존재하는 전화번호입니다.')
            #raise ValidationError('이미 존재하는 이름입니다.')
        else:
            self.username = username
            self.email = email
            self.password = PasswordHasher().hash(password)
            self.password_confirm = password_confirm
            self.user_phone = user_phone

#비밀번호 찾기 폼 passwordresetform 커스텀
class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
    max_length=254,
    widget=forms.EmailInput(attrs={'class': 'input_margin', 
                                   'autocomplete' : 'email',
                                   'placeholder' : '이메일 입력'})
    )


#비밀번호 초기화 폼 setpasswordform 커스텀
class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'new_pw', "autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'new_pw', "autocomplete": "new-password"}),
    )
