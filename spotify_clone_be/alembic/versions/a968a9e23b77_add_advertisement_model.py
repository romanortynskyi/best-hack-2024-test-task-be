"""Add Advertisement model

Revision ID: a968a9e23b77
Revises: 2ad562ff8c81
Create Date: 2024-04-28 12:40:21.019529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'a968a9e23b77'
down_revision: Union[str, None] = '2ad562ff8c81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.create_table('advertisements',
    sa.Column('id', sa.Integer(), nullable = False),
    sa.Column('created_at', sa.DateTime(timezone = True), server_default = sa.text('now()'), nullable = True),
    sa.Column('updated_at', sa.DateTime(timezone = True), server_default = sa.text('now()'), nullable = True),
    sa.Column('first_name', sa.String(length = 255), nullable = False),
    sa.Column('last_name', sa.String(length = 255), nullable = False),
    sa.Column('phone_number', sa.String(length = 255), nullable = False),
    sa.Column('city', sa.String(length = 255), nullable = False),
    sa.Column('description', sa.String(length = 255), nullable = False),
    sa.Column('user_id', sa.Integer(), nullable = False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
  )
  

def downgrade() -> None:
  op.drop_table('advertisement')
