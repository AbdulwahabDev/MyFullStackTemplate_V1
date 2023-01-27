"""____01_add_userstypetable

Revision ID: 3ad420379cc6
Revises: 
Create Date: 2022-11-16 00:12:22.692232

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ad420379cc6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "usertype",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
        sa.Column("name", sa.String , unique=True),
    )


def downgrade():
    op.drop_table("usertype")
