from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.dialects.postgresql.base import PGDialect

PGDialect._get_server_version_info = lambda *args: (16, 3)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
