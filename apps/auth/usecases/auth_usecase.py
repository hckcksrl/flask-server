import requests

from apps.auth.helpers import Kakao, JsonToken


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
