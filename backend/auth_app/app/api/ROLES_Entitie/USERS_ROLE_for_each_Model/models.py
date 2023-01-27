from datetime import datetime

import sqlalchemy as sa
from commons.db import Base
from commons.utils.generate_random_id_uuid import generate_random_uuid


class USERS_ROLE_for_each_Model(Base):
    __tablename__ = "users_role_for_each_model"
    __table_args__ = {'extend_existing': True}

    log_id = sa.Column(sa.String , default=generate_random_uuid)
    user_id = sa.Column(sa.String, primary_key=True )
    model_id = sa.Column(sa.String, primary_key=True )
    role_id = sa.Column(sa.String, primary_key=True ) 
    note = sa.Column(sa.String,nullable=True)
    created = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
    updated = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
