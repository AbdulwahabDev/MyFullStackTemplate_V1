"""____03_add_user_usertype_table

Revision ID: 15682da62788
Revises: c7fa706828d7
Create Date: 2022-11-16 02:18:55.456417

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15682da62788'
down_revision = 'c7fa706828d7'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "user_usertype",
        sa.Column("user_id", sa.String, primary_key=True),
        sa.Column("usertype_id", sa.String, primary_key=True),
        sa.Column("note", sa.String),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
    )

    op.create_foreign_key(
        constraint_name="fk_user_usertype_users",
        source_table="user_usertype",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
    )
    op.create_foreign_key(
        constraint_name="fk_user_usertype_usertype",
        source_table="user_usertype",
        referent_table="usertype",
        local_cols=["usertype_id"],
        remote_cols=["id"],
    )


def downgrade():
    op.drop_constraint("fk_user_usertype_users")
    op.drop_constraint("fk_user_usertype_usertype")
    op.drop_table("user_usertype")
