"""initial schema

Revision ID: a0e8ee2055e1
Revises: 0e778a5fa150
Create Date: 2026-06-01 19:46:28.465385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0e8ee2055e1'
down_revision: Union[str, Sequence[str], None] = '0e778a5fa150'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
