from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from settings import config_secret

engine = create_engine(f'mysql+pymysql://'
                       f'{config_secret["DB_ROOT"]}:'
                       f'{config_secret["DB_PASSWORD"]}@'
                       f'{config_secret["DB_HOST"]}:3306/'
                       f'{config_secret["DB_NAME"]}',
                       echo=True
                       )

session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
