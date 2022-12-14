import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

from .enums import LoggingLevel

logger = logging.getLogger(__name__)
import sys, os


POSTGRES_CONNECTION = "postgresql://{user}:{password}@{host}:{port}/{database}"


class CommonBaseConfig(BaseSettings):
    production: bool = False
    testing: bool = False
    ENVIRONMENT: str = "default"
    default_allow_origins = ["*"]
    APP_NAME: str = "common"
    ALLOWED_HOSTS: list[str] = ["*"]

    FORWARDED_ALLOW_IPS: str = "*"

    @property
    def allow_hosts(self):
        """
        a,b,c => ['a','b','c']
        """
        if os.environ.get("ALLOWED_HOSTS") is None:
            return self.default_allow_origins
        else:
            return os.environ.get("ALLOWED_HOSTS").split(",")

    @property
    def allow_core_origins(self):
        if os.environ.get("ALLOWED_CORS_ORIGINS") is None:
            return self.default_allow_origins
        else:
            return os.environ.get("ALLOWED_CORS_ORIGINS").split(",")

    # to disable docs if = None
    openapi_url: str = "/openapi.json"
    docs_url: str = "/docs"
  
    # db configs
    DB_USER: str =     os.environ.get('POSTGRES_USER')
    DB_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    DB_NAME: str =     None # IT WILL CHANGE BASED ON YOU BACKEND APP
    DB_HOST: str =     os.environ.get('DB_HOST')
    DB_PORT: int =     int(os.environ.get('DB_PORT') )

    # read only db configs
    READ_ONLY_DB_USER: str | None = os.environ.get('POSTGRES_USER')
    READ_ONLY_DB_PASSWORD: str | None = os.environ.get('POSTGRES_PASSWORD')
    READ_ONLY_DB_NAME: str | None = None # IT WILL CHANGE BASED ON YOU BACKEND APP
    READ_ONLY_DB_HOST: str | None = os.environ.get('DB_HOST')
    READ_ONLY_DB_PORT: int | None = int(os.environ.get('DB_PORT') )
  
    # logging level ,,
    LOGGING_LEVEL: LoggingLevel = LoggingLevel.INFO

    # the current head git sha ,, used to track deployments
    RELEASE_SHA: str = "unknown"

    # generate SQLALCHEMY_DATABASE_URL dynamically
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str: 
        return POSTGRES_CONNECTION.format(
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
        )

    @property
    def SQLALCHEMY_READ_DATABASE_URL(self) -> str: 
        if self.READ_ONLY_DB_USER is not None:
            return POSTGRES_CONNECTION.format(
                user=self.READ_ONLY_DB_USER,
                password=self.READ_ONLY_DB_PASSWORD,
                host=self.READ_ONLY_DB_HOST,
                port=self.READ_ONLY_DB_PORT,
                database=self.READ_ONLY_DB_NAME,
            )
        else:
            return self.SQLALCHEMY_DATABASE_URL

    SQL_POOL_SIZE: int = 40
    SQL_POOL_OVERFLOW_SIZE: int = 10
    SQL_POOL_ENABLED: bool = True

    class Config:
        env_file = ".env"


# you can set the defaults from here or over ride all using .env


class CommonProductionConfig(BaseSettings):
    production = True
    testing = False
    ENVIRONMENT = "prod"
    openapi_url: str | None = None


class CommonStagingConfig(BaseSettings):
    production = True
    testing = False
    ENVIRONMENT = "staging"
    LOGGING_LEVEL: LoggingLevel = LoggingLevel.DEBUG


class CommonTestingConfig(BaseSettings):
    production = False
    testing = True
    ENVIRONMENT = "testing"
    SQL_POOL_ENABLED = False


@lru_cache()
def current_config(ProductionConfig, StagingConfig, TestingConfig, BaseConfig):
    """
    this will load the required config passed on STAGE env if not set it will load LocalConfig
    """
    stage = os.environ.get("ENVIRONMENT", "local")
    stage_to_config_map = {
        "prod": ProductionConfig,
        "staging": StagingConfig,
        "testing": TestingConfig,
        "local": BaseConfig,
    }
    if stage not in stage_to_config_map:
        raise Exception(f"ENVIRONMENT: {stage} is not supported")

    logger.info(f"loading {stage} Config...")
    return stage_to_config_map[stage]()
