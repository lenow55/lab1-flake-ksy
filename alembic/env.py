import asyncio
from logging.config import fileConfig

import alembic_postgresql_enum
from sqlalchemy import URL, pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context

# это объект конфигурации Alembic, который предоставляет
# доступ к значениям в используемом .ini файле.
config = context.config

alembic_postgresql_enum.set_configuration(alembic_postgresql_enum.Config())

# добавьте сюда объект MetaData вашей модели
# для поддержки 'autogenerate'
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from src.schemas.metadata import metadata_obj  # noqa: E402
from src.config import Settings  # noqa: E402

target_metadata = metadata_obj

# загрузим конфигурацию из переменных окружения
# с параметрами подклчюения к базе данных
app_config = Settings()

# другие значения из конфигурации, определенные потребностями env.py,
# могут быть получены:
# my_important_option = config.get_main_option("my_important_option")
# ... и т.д.


def run_migrations_offline() -> None:
    """Запуск миграций в 'офлайн' режиме.

    Это настраивает контекст только с URL,
    без Engine, хотя Engine также приемлем
    здесь. Пропуская создание Engine,
    нам даже не нужен доступный DBAPI.

    Вызовы context.execute() здесь выводят заданную строку в
    вывод скрипта.

    """
    url = URL.create(
        app_config.dialect,
        username=app_config.db_user,
        password=app_config.db_password.get_secret_value(),
        host=app_config.db_host,
        database=app_config.db_name,
        port=app_config.db_port,
    )
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """В этом сценарии нам нужно создать Engine
    и связать соединение с контекстом.

    """

    url_object = URL.create(
        app_config.dialect,
        username=app_config.db_user,
        password=app_config.db_password.get_secret_value(),
        host=app_config.db_host,
        database=app_config.db_name,
        port=app_config.db_port,
    )
    connectable = create_async_engine(
        url_object,
        echo=app_config.sql_command_echo,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
