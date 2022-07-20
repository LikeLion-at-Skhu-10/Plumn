from distutils.command.clean import clean
from django import forms
from .models import User
from argon2 import PasswordHasher

class RegisterForm(forms.ModelForm):
    user_id = forms.CharFIeld(
        label='아이디',
        requried=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={
            'required' : '아이디를 입력해 주세요.',
            'unique' : '중복된 아이디입니다.'}
    )

    user_pwd = forms.CharFIeld(
        label='비밀번호',
        requried=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pwd',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해 주세요.'}
    )

    user_pwd_confirm = forms.CharFIeld(
        label='비밀번호 확인',
        requried=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pwd-confirm',
                'placeholder' : '비밀번호 확인'
            }
        ),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )

    user_name = forms.CharField(
        label='이름',
        requried=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-name',
                'placeholder' : '이름'
            }
        ),
        error_messages={'required' : '닉네임을 입력해 주세요.'}
    )    

    user_phone = forms.CharFIeld(
        label='전화번호',
        requried=True,
        widget=forms.CharField(
            attrs={
                'class' : 'user-phone',
                'placeholder' : '전화번호'
            }
        ),
        error_messages={
            'required' : '올바른 전화번호를 입력해 주세요.',
            'unique' : '중복된 전화번호 입니다.'}
    )    
    
    field_order = [
        'user_name',
        'user_id'
        'user_pwd',
        'user_pwd-confirm',
        'user_phone',
    ]
    
    class Meta:
        model = User
        fields = [
            'user_id',
            'user_pwd',
            'user_name',
            'user_phone',
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        
        user_id = cleaned_data.get('user_id', '')
        user_pwd = cleaned_data.get('user_pwd', '')
        user_pwd_confirm = cleaned_data.get('user_pwd_confirm', '')
        user_name = cleaned_data.get('user_name', '')
        user_phone = cleaned_data.get('user_phone', '')
        
        if user_pwd != user_pwd_confirm:
            return self.add_error('user_pwd_confirm', '비밀번호가 다릅니다.')
        elif not (4 <= len(user_id) <= 16):
            return self.add_error('user_id', '아이디는 4~16자로 입력해 주세요.')
        elif 8 > len(user_pwd):
            return self.add_error('user_pwd', '비밀번호는 8자 이상으로 적어주세요.')
        else:
            self.user_id = user_id
            self.user_pwd = PasswordHasher().hash(user_pwd)
            self.user_pwd_confirm = user_pwd_confirm
            self.user_name = user_name
            self.user_phone = user_phone