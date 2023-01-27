from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from pydantic import BaseSettings
from .enums import LoggingLevel

import os


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


def set_up_main(config: CommonBaseConfig, routers_modules: list = []):
    app = FastAPI(
        debug=not config.production,
        title=f"{config.APP_NAME}({config.ENVIRONMENT}-{config.RELEASE_SHA})",
        openapi_url=config.openapi_url,
        docs_url=config.docs_url,
    )

    app.add_middleware(GZipMiddleware)
    app.add_middleware(ProxyHeadersMiddleware, trusted_hosts=config.FORWARDED_ALLOW_IPS)
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=config.allow_hosts)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
                        "http://localhost","http://localhost:3000","http://localhost:3006","http://localhost:4200",
                       "http://127.0.0.1","http://127.0.0.1:3000","http://127.0.0.1:3006","http://127.0.0.1:4200",
                    #    "http://0.0.0.0","http://0.0.0.0:3000","http://0.0.0.0:3006"
                       ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
 

 

    for router_module in routers_modules:
        app.include_router(router_module)

    
    # for nested routes docs
    for path_k, path_v in app.openapi()["paths"].items():
        for method_k, method_v in path_v.items():
            if len(method_v["tags"]) > 1:
                method_v["tags"] = [method_v["tags"][-1]]

    return app
