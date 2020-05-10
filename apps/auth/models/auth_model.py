from sqlalchemy import Column, Integer, String
from settings.database import Base


class Auth(Base):
    __tablename__ = 'auth'

    id = Column(Integer, primary_key=True)
    access_token = Column(String, nullable=False)
    email = Column(String, unique=True)
    social = Column(String, nullable=False)
    username = Column(String, nullable=False)