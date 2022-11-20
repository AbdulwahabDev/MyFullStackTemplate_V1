import os
import logging
from functools import lru_cache

logger = logging.getLogger(__name__)


from ProjectConfig import ProjectConfigClass

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

def set_up_main( routers_modules: list = []):
    app = FastAPI(
        title="{config.APP_NAME}({config.ENVIRONMENT}-{config.RELEASE_SHA})",
        # openapi_url=config.openapi_url,
        # docs_url=config.docs_url,
    )

    app.add_middleware(GZipMiddleware)
    app.add_middleware(ProxyHeadersMiddleware, trusted_hosts=["*"])
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"]) 
    app.add_middleware(CORSMiddleware,
        allow_origins=["http://localhost","http://localhost:3000","http://localhost:3006",
                       "http://127.0.0.1","http://127.0.0.1:3000","http://127.0.0.1:3006",
                       "http://0.0.0.0","http://0.0.0.0:3000","http://0.0.0.0:3006"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],)
 
      
    for router_module in routers_modules:
        app.include_router(router_module)

    # for nested routes docs
    for path_k, path_v in app.openapi()["paths"].items():
        for method_k, method_v in path_v.items():
            if len(method_v["tags"]) > 1:
                method_v["tags"] = [method_v["tags"][-1]]
    

    return app


@lru_cache()
def current_config(BaseConfig):
    """
    this will load the required config passed on STAGE env if not set it will load LocalConfig
    """
    stage = os.environ.get("ENVIRONMENT", "local")
    stage_to_config_map = {
        "local": BaseConfig,
    }
    if stage not in stage_to_config_map:
        raise Exception(f"ENVIRONMENT: {stage} is not supported")

    logger.info(f"loading {stage} Config...")
    return stage_to_config_map[stage]()

class BaseConfig():
    APP_NAME: str = ProjectConfigClass.Get_APP_NAME()
    token_APP_AUTH_URL: str =   ProjectConfigClass.Get_AUTH_APP_URL() 

config: BaseConfig = current_config(BaseConfig)
