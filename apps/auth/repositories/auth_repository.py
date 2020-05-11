from apps.auth.models import Auth
import abc
from settings.database import session


class Repository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_auth(
            self,
            id: int,
            social: str
    ):
        pass

    @abc.abstractmethod
    def create_auth(
            self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
    ):
        pass

    @abc.abstractmethod
    def update_auth(
            self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
        ):
        pass


class AuthRepository(Repository):
    def get_auth(
            self,
            id: int,
            social: str
    ):
        query = session.query(Auth).filter(Auth.id == id)

        auth = query.first()

        if not auth:
            return None

        return auth

    def create_auth(
            self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
    ):
        auth = Auth(
            email=email,
            id=id,
            social=social,
            username=username,
            access_token=access_token,
        )

        session.add(auth)
        session.commit()

        return auth

    def update_auth(
            self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
    ):
        query = session.query(Auth).filter(Auth.id == id)

        auth = query.first()

        if access_token:
            auth.access_token = access_token

        session.add(auth)
        session.commit()

        return auth
