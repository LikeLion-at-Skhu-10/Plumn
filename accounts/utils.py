# API 참조서에 따르면 header와 body에 각각 필요한 부분을 넣어서 호출해야 하며
# 호출에 필요한 예제코드도 참조서에 따라 참조
# x-ncp-apigw-signature-v2(서명)부분을 만들기 위해 utils.py를 만듦
import secrets
import hashlib
import hmac
import base64
import os, json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

#개인 정보, 개인 API 정보를 보안 문제로 secrets.json에 따로 기입했음
#따라서 아래 코드 작성
BASE_DIR = Path(__file__).resolve().parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

access_key = get_secret("SMS_ADMIN_ACCESS_KEY") #개인 API 정보 중 access key Id인데 보안 우려로 secrets.json에 입력
secret_key = get_secret("SMS_ADMIN_SECRET_KEY") #이하 동문
send_phone_number = get_secret("SEND_PHONE_NUMBER") 

uri = "/sms/v2/services/ncp:sms:kr:289439711828:sms_auth"
API_URL = 'https://sens.apigw.ntruss.com' + f'{uri}' + '/messages'
# uri 중간에 Console - Project - 해당 Project 서비스 ID 입력

def make_signature(timestamp):
    secret_key = bytes(secret_key, 'UTF-8')
    method = "POST"
    
    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingKey

