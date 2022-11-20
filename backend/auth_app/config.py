
import sys , os
sys.path.append(os.path.abspath('../'))   
from ProjectConfig import ProjectConfigClass

from commons.config import (
    CommonBaseConfig,
    CommonProductionConfig,
    CommonStagingConfig,
    CommonTestingConfig,
    current_config,
)


class BaseConfig(CommonBaseConfig):
    APP_NAME: str = "app_auth" 
    AUTH_SALT: str = ProjectConfigClass.Get_AUTH_SALT()
    AUTH_JWT_KEY: str = ProjectConfigClass.Get_AUTH_JWT_KEY()
    AUTH_TOKEN_EXPIRE_IN: int = int(ProjectConfigClass.Get_ACCESS_TOKEN_EXPIRE_IN_SECONDS())


class ProductionConfig(CommonProductionConfig, BaseConfig):  # type: ignore
    pass


class StagingConfig(CommonStagingConfig, BaseConfig):  # type: ignore
    pass


class TestingConfig(CommonTestingConfig, BaseConfig):  # type: ignore
    pass


config: BaseConfig = current_config(ProductionConfig, StagingConfig, TestingConfig, BaseConfig)
