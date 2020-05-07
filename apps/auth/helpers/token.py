import jwt


class JsonToken:
    def encode(self, payload: dict):
        token = jwt.encode(
            payload={**payload},
            key="secret",
            algorithm="HS256"
        )
        return token

    def decode(self, token: str):
        try:
            decode = jwt.decode(
                token,
                "secret",
                algorithms=["HS256"],
            )
            return decode
        except jwt.exceptions.DecodeError:
            return 'invalid token'
        except jwt.exceptions.ExpiredSignatureError:
            return 'expire token'
