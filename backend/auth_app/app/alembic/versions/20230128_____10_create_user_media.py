"""____10_create_user_media

Revision ID: e2ae1ce33701
Revises: 769b333cd705
Create Date: 2023-01-28 04:44:39.810317

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2ae1ce33701'
down_revision = '769b333cd705'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        "user_media",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("user_id", sa.String, nullable=False),
        sa.Column("media_type_id", sa.String, nullable=False),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
        sa.Column("name", sa.String, nullable=False, unique=True), 
        sa.Column("URL", sa.String, nullable=True),
  
    )

    op.create_foreign_key(
        constraint_name="fk_user_media_user",
        source_table="user_media",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
    )

    op.create_foreign_key(
        constraint_name="fk_user_media_media_type",
        source_table="user_media",
        referent_table="media_type",
        local_cols=["media_type_id"],
        remote_cols=["id"],
    )

def downgrade():
    op.drop_constraint("fk_user_media_user") 
    op.drop_constraint("fk_user_media_media_type") 
    op.drop_table("user_media") 


 