from datetime import datetime

import sqlalchemy as sa
from commons.db import Base


class user_UserType(Base):
    __tablename__ = "user_usertype"
    __table_args__ = {'extend_existing': True}

    user_id = sa.Column(sa.String, primary_key=True)
    usertype_id = sa.Column(sa.String, primary_key=True)
    note = sa.Column(sa.String)
    created = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
    updated = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
