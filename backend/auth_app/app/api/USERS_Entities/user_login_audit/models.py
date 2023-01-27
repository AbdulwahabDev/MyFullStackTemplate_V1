from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped , relationship

from commons.db import Base
from commons.utils.generate_random_id_uuid import generate_random_uuid


class User_Login_Audit(Base):
    __tablename__ = "user_login_audit"
    __table_args__ = {'extend_existing': True}

    log_id: Mapped[str] = sa.Column(sa.String, primary_key=True, nullable=False, default=generate_random_uuid)
    user_id: Mapped[str] = sa.Column(sa.String, nullable=False)
    user_name: Mapped[str] = sa.Column(sa.String, nullable=False)
    name: Mapped[str] = sa.Column(sa.String, nullable=False)
    note: Mapped[str] = sa.Column(sa.String, nullable=False)
    created: Mapped[datetime] = sa.Column(sa.DateTime, default=datetime.now, nullable=False)


    # owner = relationship("backend.auth_app.app.api.USERS_Entities.users.models.Users", back_populates="loging_log")
