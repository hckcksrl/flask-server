import requests

from apps.auth.helpers import Kakao, JsonToken, FaceBook
from apps.auth.repositories import AuthRepository


class AuthUseCase:
    def __init__(self):
        self.repository = AuthRepository()


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

        auth = self.repository.get_auth(id=response.get('id'), social='kakao')

        if auth:
            self.repository.update_auth(
                access_token=access_token,
                id=response.get('id'),
                email=response.get('kakao_account').get('email'),
                social='kakao',
                username=response.get('properties').get('nickname')
            )
        else:
            auth =self.repository.create_auth(
                access_token=access_token,
                id=response.get('id'),
                email=response.get('kakao_account').get('email'),
                social='kakao',
                username=response.get('properties').get('nickname')
            )

        token = JsonToken().encode(
            payload={"id": auth.id}
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

        auth = self.repository.get_auth(id=response.get('id'), social='facebook')

        if auth:
            self.repository.update_auth(
                access_token=access_token,
                id=response.get('id'),
                email=response.get('email'),
                social='facebook',
                username=response.get('name')
            )
        else:
            auth = self.repository.create_auth(
                access_token=access_token,
                id=response.get('id'),
                email=response.get('email'),
                social='facebook',
                username=response.get('name')
            )

        token = JsonToken().encode(
            payload={"id": auth.id}
        )

        return token.decode('utf-8')

