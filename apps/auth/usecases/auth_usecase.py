import requests

from apps.auth.helpers import Kakao, JsonToken, FaceBook


class AuthUseCase:
    def __init__(self):
        pass


class KakaoAuthUseCase(AuthUseCase):
    def execute(self, code: str):
        access_response = requests.post(
            url="https://kauth.kakao.com/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": Kakao.kakao_api_id,
                "redirect_uri": Kakao.kakao_api_redirect_uri,
                "code": code
            }
        ).json()

        error = access_response.get("error", None)

        if error:
            raise Exception

        access_token = access_response.get('access_token')

        header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(
            url="https://kapi.kakao.com/v2/user/me",
            headers=header
        ).json()

        token = JsonToken().encode(
            payload={"id": response.get('id')}
        )

        return token.decode('utf-8')


class FaceBookUseCase(AuthUseCase):
    def execute(self, code: dict):
        access_response = requests.get(
            url='https://graph.facebook.com/v6.0/oauth/access_token',
            params={
                "client_id": FaceBook.facebook_api_id,
                "redirect_uri": FaceBook.facebook_api_redirect_uri,
                "client_secret": FaceBook.facebook_api_secret,
                "code": code,
            },
        ).json()

        error = access_response.get("error", None)

        if error:
            raise Exception

        access_token = access_response.get('access_token')

        response = requests.get(
            url='https://graph.facebook.com/me',
            params={
                "access_token": access_token,
                "fields": "email,name"
            },
        ).json()

        token = JsonToken().encode(
            payload={"id": response['id']}
        )

        return token.decode('utf-8')

