from sqlalchemy import Column, Integer, String
from settings.database import Base


class Auth(Base):
    __tablename__ = 'auth'

    id = Column(Integer, primary_key=True)
    access_token = Column(String(length=1000), nullable=False)
    email = Column(String(length=255), unique=True)
    social = Column(String(length=255), nullable=False)
    username = Column(String(length=255), nullable=False)
