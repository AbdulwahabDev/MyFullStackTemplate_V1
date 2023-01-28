"""____08_create_user_phone

Revision ID: c10d2d7c967c
Revises: b54572da358f
Create Date: 2023-01-28 03:00:26.510405

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c10d2d7c967c'
down_revision = 'b54572da358f'
branch_labels = None
depends_on = None


 


def upgrade():
    op.create_table(
        "user_phone",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
        sa.Column("phone", sa.String, nullable=False, unique=True), 
        sa.Column("note", sa.String, nullable=True),
 
        sa.Column("user_id", sa.String, nullable=False),
    )

    op.create_foreign_key(
        constraint_name="fk_user_phone_users",
        source_table="user_phone",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
    )

def downgrade():
    op.drop_constraint("fk_user_phone_users") 
    op.drop_table("user_phone") 
