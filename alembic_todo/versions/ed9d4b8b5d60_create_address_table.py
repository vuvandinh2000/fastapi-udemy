"""create address table

Revision ID: ed9d4b8b5d60
Revises: 303f395b63a3
Create Date: 2023-03-25 17:56:39.663752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed9d4b8b5d60'
down_revision = '303f395b63a3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("address",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("address1", sa.String(), nullable=False),
                    sa.Column("address2", sa.String(), nullable=False),
                    sa.Column("city", sa.String(), nullable=False),
                    sa.Column("state", sa.String(), nullable=False),
                    sa.Column("country", sa.String(), nullable=False),
                    sa.Column("postalcode", sa.String(), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table("address")
