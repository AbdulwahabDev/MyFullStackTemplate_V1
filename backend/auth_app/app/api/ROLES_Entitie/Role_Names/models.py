from datetime import datetime

import sqlalchemy as sa
from commons.db import Base
from commons.utils.generate_random_id_uuid import generate_random_uuid


class Role_Names(Base):
    __tablename__ = "role_names"
    __table_args__ = {'extend_existing': True}

    role_id = sa.Column(sa.String, primary_key=True , default=generate_random_uuid)
    name = sa.Column(sa.String,nullable=False) 
    note = sa.Column(sa.String,nullable=True)
    created = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
    updated = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
