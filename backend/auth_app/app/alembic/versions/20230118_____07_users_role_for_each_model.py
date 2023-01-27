"""____07_USERS_ROLE_for_each_Model

Revision ID: b54572da358f
Revises: 0b5cfe84a667
Create Date: 2023-01-18 21:45:38.227276

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b54572da358f'
down_revision = '0b5cfe84a667'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "users_role_for_each_model", 
        sa.Column("log_id", sa.String),
        sa.Column("user_id", sa.String, primary_key=True),
        sa.Column("model_id", sa.String, primary_key=True),
        sa.Column("role_id", sa.String, primary_key=True),
        sa.Column("note", sa.String),
        sa.Column("created", sa.DateTime, nullable=False, default=datetime.now),
        sa.Column("updated", sa.DateTime, onupdate=datetime.now),
    )

    op.create_foreign_key(
        constraint_name="fk_users_role_for_each_model____users",
        source_table="users_role_for_each_model",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
    )
    op.create_foreign_key(
        constraint_name="fk_users_role_for_each_model____role_models",
        source_table="users_role_for_each_model",
        referent_table="role_models",
        local_cols=["model_id"],
        remote_cols=["model_id"],
    )
    op.create_foreign_key(
        constraint_name="fk_users_role_for_each_model____role_names",
        source_table="users_role_for_each_model",
        referent_table="role_names",
        local_cols=["role_id"],
        remote_cols=["role_id"],
    )


def downgrade():
    op.drop_constraint("fk_users_role_for_each_model____users")
    op.drop_constraint("fk_users_role_for_each_model____role_models")
    op.drop_constraint("fk_users_role_for_each_model____role_names")
    op.drop_table("users_role_for_each_model")
