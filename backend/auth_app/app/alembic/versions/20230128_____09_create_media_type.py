"""____09_create_media_type

Revision ID: 769b333cd705
Revises: c10d2d7c967c
Create Date: 2023-01-28 04:23:02.139007

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '769b333cd705'
down_revision = 'c10d2d7c967c'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        "media_type",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("note", sa.String),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
    )


def downgrade():
    op.drop_table("media_type")
     
