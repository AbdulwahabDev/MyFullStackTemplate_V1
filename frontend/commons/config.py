import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

from .enums import LoggingLevel

logger = logging.getLogger(__name__)
import sys, os
sys.path.append(os.path.abspath('../'))  
from ProjectConfig import ProjectConfigClass
 


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
   
    # logging level ,,
    LOGGING_LEVEL: LoggingLevel = LoggingLevel.INFO

    # the current head git sha ,, used to track deployments
    RELEASE_SHA: str = "unknown"
  
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
