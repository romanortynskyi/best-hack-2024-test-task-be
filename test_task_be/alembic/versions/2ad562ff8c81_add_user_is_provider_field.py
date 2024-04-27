"""Add User is_provider field

Revision ID: 2ad562ff8c81
Revises: 0a759cdbab43
Create Date: 2024-04-27 11:48:16.865421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ad562ff8c81'
down_revision: Union[str, None] = '0a759cdbab43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.add_column('users', sa.Column('is_provider', sa.Boolean(), nullable=False))

def downgrade() -> None:
  op.drop_column('users', 'is_provider')
