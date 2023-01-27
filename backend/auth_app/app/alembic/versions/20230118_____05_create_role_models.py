"""____05_create_role_models

Revision ID: 2b116b5048c9
Revises: a5d3fe28814f
Create Date: 2023-01-18 20:15:15.330436

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b116b5048c9'
down_revision = 'a5d3fe28814f'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        "role_models",
        sa.Column("model_id", sa.String, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("note", sa.String),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
    )


def downgrade():
    op.drop_table("role_models")
     
