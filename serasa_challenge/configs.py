from typing import Literal
from typing import Optional

import pydantic

from sqlalchemy.engine.url import URL


class Settings(pydantic.BaseSettings):
    # Project
    PROJECT_NAME: str = "serasa_challenge"
    DEBUG: bool = False

    # Server
    SERVER_PORT: int
    SERVER_HOST: str
    SERVER_LOG_LEVEL: str = "info"

    # Tests
    TESTING: bool

    # Database
    DB_HOST: str
    DEFAULT_DB_DRIVER: str = "postgresql"
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int = 5432
    DB_SSL_REQUIRE: Literal["disable", "prefer", "allow", "require", "verify-ca", "verify-full"] = "disable"
    DB_LOG_LEVEL: str = "info"
    DB_ECHO: bool = False
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 0

    @property
    def DB_URI(self) -> str:
        return str(
            URL.create(
                drivername=self.DEFAULT_DB_DRIVER,
                username=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT,
                database=self.DB_NAME,
            )
        )

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
