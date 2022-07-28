#회원가입을 이메일 인증으로 하기 위한 토큰파일
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (str(user.pk) + str(timestamp)) +  str(user.is_active)

account_activation_token = AccountActivationTokenGenerator()