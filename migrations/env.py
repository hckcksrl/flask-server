from logging.config import fileConfig
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context

root_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(root_dir)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

fileConfig(config.config_file_name)
from apps.auth.models import *
from settings.database import Base
from settings import config_secret

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=f'mysql+pymysql://'
            f'{config_secret["DB_ROOT"]}:'
            f'{config_secret["DB_PASSWORD"]}@'
            f'{config_secret["DB_HOST"]}/'
            f'{config_secret["DB_NAME"]}',
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(
        f'mysql+pymysql://'
        f'{config_secret["DB_ROOT"]}:'
        f'{config_secret["DB_PASSWORD"]}@'
        f'{config_secret["DB_HOST"]}:3306/'
        f'{config_secret["DB_NAME"]}',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
