
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

POSTGRES_CONNECTION = "postgresql://{user}:{password}@{host}:{port}/{database}"

class BaseConfig(CommonBaseConfig):
    APP_NAME: str = "auth_app"
    RELEASE_SHA: str = "0.0.1"
    DB_NAME: str = "template_auth_app_db"                  # MUST BE LOWER CASE 
    READ_ONLY_DB_NAME: str = "template_auth_app_db"        # MUST BE LOWER CASE 
    
    AUTH_SALT: str = ProjectConfigClass.Get_AUTH_SALT()
    AUTH_JWT_KEY: str = ProjectConfigClass.Get_AUTH_JWT_KEY()
    Get_HASH_ALGORITHM: str = ProjectConfigClass.Get_HASH_ALGORITHM()
    AUTH_TOKEN_EXPIRE_IN: int = int(ProjectConfigClass.Get_ACCESS_TOKEN_EXPIRE_IN_SECONDS())

class ProductionConfig(CommonProductionConfig, BaseConfig):  # type: ignore
    pass


class StagingConfig(CommonStagingConfig, BaseConfig):  # type: ignore
    pass


class TestingConfig(CommonTestingConfig, BaseConfig):  # type: ignore
    pass


config: BaseConfig = current_config(ProductionConfig, StagingConfig, TestingConfig, BaseConfig)
