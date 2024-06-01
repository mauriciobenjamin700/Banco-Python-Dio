"""update

Revision ID: 860e4e37669d
Revises: da705bb019dc
Create Date: 2024-06-01 11:18:01.199904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '860e4e37669d'
down_revision: Union[str, None] = 'da705bb019dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Renomear coluna 'account_number' para 'id'
    op.alter_column('account', 'account_number', new_column_name='id', existing_type=sa.Integer(), nullable=False)

    # Ajustar outras colunas conforme necessário
    op.alter_column('client', 'name',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('client', 'login',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('client', 'password',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.drop_column('client', 'abacate')


def downgrade() -> None:
    # Reverter nome da coluna de 'id' para 'account_number'
    op.alter_column('account', 'id', new_column_name='account_number', existing_type=sa.Integer(), nullable=False)

    # Reverter outras alterações conforme necessário
    op.add_column('client', sa.Column('abacate', sa.VARCHAR(length=30), nullable=True))
    op.alter_column('client', 'password',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
    op.alter_column('client', 'login',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
    op.alter_column('client', 'name',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
