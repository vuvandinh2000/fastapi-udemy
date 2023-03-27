"""add column aptnum

Revision ID: 28f82a290ce3
Revises: ffec9ab3287d
Create Date: 2023-03-25 23:40:15.590909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f82a290ce3'
down_revision = 'ffec9ab3287d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
