"""create addressid to users

Revision ID: ffec9ab3287d
Revises: ed9d4b8b5d60
Create Date: 2023-03-25 18:01:49.350975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffec9ab3287d'
down_revision = 'ed9d4b8b5d60'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key("address_users_fk", source_table="users", referent_table="address",
                          local_cols=["address_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")
