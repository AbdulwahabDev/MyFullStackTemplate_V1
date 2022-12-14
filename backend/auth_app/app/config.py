
import sys , os


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
    DB_NAME: str = "myfullstacktemplate_v1_auth_app_db"
    READ_ONLY_DB_NAME: str = "myfullstacktemplate_v1_auth_app_db"
    
    AUTH_SALT: str = os.environ.get('AUTH_SALT') 
    AUTH_JWT_KEY: str = os.environ.get('AUTH_JWT_KEY')
    Get_HASH_ALGORITHM: str = os.environ.get('HASH_ALGORITHM') 
    AUTH_TOKEN_EXPIRE_IN: int = int(os.environ.get('ACCESS_TOKEN_EXPIRE_IN_SECONDS'))

class ProductionConfig(CommonProductionConfig, BaseConfig):  # type: ignore
    pass


class StagingConfig(CommonStagingConfig, BaseConfig):  # type: ignore
    pass


class TestingConfig(CommonTestingConfig, BaseConfig):  # type: ignore
    pass


config: BaseConfig = current_config(ProductionConfig, StagingConfig, TestingConfig, BaseConfig)
