import json
from datetime import date, datetime, time
from sqlalchemy.future.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

from .config import CommonBaseConfig

DELETE_DATETIME = datetime.fromtimestamp(0)


def datetime_encoder(val):
    if isinstance(val, date):
        return val.isoformat()

    if isinstance(val, time):
        return val.isoformat()

    raise TypeError()


class BaseDb(object):
    def __init__(self, config: CommonBaseConfig):
        engine_options = {
            "echo": False,
            "echo_pool": False,
            "poolclass": StaticPool,  # no pooling from sqlalchemy
            "future": True,
            "json_serializer": lambda obj: json.dumps(obj, default=datetime_encoder),
        }

        if config.SQL_POOL_ENABLED:
            engine_options.update(
                {
                    "pool_size": config.SQL_POOL_SIZE,
                    "max_overflow": config.SQL_POOL_OVERFLOW_SIZE,
                }
            )
            del engine_options["poolclass"]

        self.engine = create_engine(config.SQLALCHEMY_DATABASE_URL, **engine_options)  # type: ignore[arg-type, call-overload]
        self.read_engine = create_engine(config.SQLALCHEMY_READ_DATABASE_URL, **engine_options)  # type: ignore[arg-type, call-overload]

        from sqlalchemy import create_engine as create_engine_old_way
        self.Custome_read_engine = create_engine_old_way(config.SQLALCHEMY_READ_DATABASE_URL, **{"echo":False,"future":False})  # type: ignore[arg-type, call-overload]
        # type: ignore[arg-type, call-overload]
        # following https://fastapi.tiangolo.com/tutorial/sql-databases
        sessionmaker_optins = {
            "autocommit": False,
            "autoflush": False,
            "expire_on_commit": False,
            "future": True,
        }

        self.SessionLocal = sessionmaker(bind=self.engine, **sessionmaker_optins)  # type: ignore[arg-type, call-overload]
        self.ReadSessionLocal = sessionmaker(bind=self.read_engine, **sessionmaker_optins)  # type: ignore[arg-type, call-overload]


Base = declarative_base()
