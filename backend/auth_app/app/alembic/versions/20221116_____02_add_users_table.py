"""____02_add_users_table

Revision ID: c7fa706828d7
Revises: 3ad420379cc6
Create Date: 2022-11-16 00:15:40.053541

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7fa706828d7'
down_revision = '3ad420379cc6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users_status_type",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
        sa.Column("name", sa.String, nullable=False), 
        sa.Column("note", sa.String, nullable=False),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("username", sa.String, nullable=False, unique=True),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("is_active", sa.String, nullable=False, default=True),
        sa.Column("password", sa.String, nullable=False),
 
        sa.Column("status_id", sa.String, nullable=False, default=False),
    )

    op.create_foreign_key(
        constraint_name="fk_users_users_status_type",
        source_table="users",
        referent_table="users_status_type",
        local_cols=["status_id"],
        remote_cols=["id"],
    )

def downgrade():
    op.drop_constraint("fk_users_users_status_type")

    op.drop_table("users_status_type")
    op.drop_table("users")
