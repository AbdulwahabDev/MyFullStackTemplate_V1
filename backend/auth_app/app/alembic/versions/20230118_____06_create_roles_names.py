"""____06_create_roles_names

Revision ID: 0b5cfe84a667
Revises: 2b116b5048c9
Create Date: 2023-01-18 21:26:09.808334

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b5cfe84a667'
down_revision = '2b116b5048c9'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        "role_names",
        sa.Column("role_id", sa.String, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("note", sa.String),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
    )

def downgrade():
    op.drop_table("role_names")
