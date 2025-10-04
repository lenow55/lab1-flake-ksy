import os

from typing import ClassVar

from pydantic import Field, SecretStr
from pydantic.functional_validators import BeforeValidator
from pydantic_settings import (
    BaseSettings,
    JsonConfigSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)
from typing_extensions import Annotated


def convert_str2int(v):
    if isinstance(v, str):
        v = int(v)
    return v


IntMapStr = Annotated[int, BeforeValidator(convert_str2int)]


class Settings(BaseSettings):
    dialect: str = Field(default="postgresql+asyncpg")
    db_host: str = Field(default="localhost")
    db_port: IntMapStr = Field(default=5432)
    db_user: str = Field(default="user")
    db_name: str = Field(default="db")
    db_password: SecretStr = Field(default=SecretStr(""))
    sql_command_echo: bool = Field(default=False)

    @property
    def db_connect_url(self) -> str:
        """
        полный url для подключения к postgresql
        """
        s = f"{self.dialect}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        return s

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        json_file=("config.json", "debug_config.json")
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            JsonConfigSettingsSource(settings_cls),
            dotenv_settings,
            file_secret_settings,
        )
