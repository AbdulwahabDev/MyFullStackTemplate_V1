from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped , relationship

from commons.db import Base
from commons.utils.generate_random_id_uuid import generate_random_uuid


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id: Mapped[str] = sa.Column(sa.String, primary_key=True, default=generate_random_uuid)
    created: Mapped[datetime] = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
    updated: Mapped[datetime] = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    name: Mapped[str] = sa.Column(sa.String, nullable=False)
    username: Mapped[str] = sa.Column(sa.String, nullable=False, unique=True)
    email: Mapped[str] = sa.Column(sa.String, nullable=False, unique=True)
    is_active: Mapped[bool] = sa.Column(sa.BOOLEAN, nullable=True, default=True)
    is_online: Mapped[bool] = sa.Column(sa.BOOLEAN, nullable=True, default=False)
    password: Mapped[str] = sa.Column(sa.String, nullable=False)
    photo: Mapped[str] = sa.Column(sa.String, nullable=True, default="assets/media/avatars/blank.png")

    # loging_log = relationship("backend.auth_app.app.api.USERS_Entities.user_login_audit.models.User_Login_Audit", back_populates="owner")
