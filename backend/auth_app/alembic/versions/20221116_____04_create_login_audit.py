"""____04_create_login_audit

Revision ID: a5d3fe28814f
Revises: 15682da62788
Create Date: 2022-11-16 02:24:23.257931

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5d3fe28814f'
down_revision = '15682da62788'
branch_labels = None
depends_on = None


def upgrade():    
    op.create_table(
        "user_login_audit",
        sa.Column("log_id", sa.String, primary_key=True),
        sa.Column("user_id", sa.String),
        sa.Column("user_name", sa.String),
        sa.Column("name", sa.String),
        sa.Column("note", sa.String),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
    )

def downgrade():
    op.drop_table("user_login_audit")
