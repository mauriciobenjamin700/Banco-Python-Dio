"""Remove abacate column to client table

Revision ID: e4e994642cd7
Revises: ce4f4e618919
Create Date: 2024-05-31 10:31:47.430211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4e994642cd7'
down_revision: Union[str, None] = 'ce4f4e618919'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('client', 'abacate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('abacate', sa.VARCHAR(length=30), nullable=True))
    # ### end Alembic commands ###
