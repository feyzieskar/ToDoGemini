"""phone number added

Revision ID: 1ba4a6dcddcc
Revises: 
Create Date: 2025-01-13 23:51:25.724650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ba4a6dcddcc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    #op.drop_column("users", "phone_number")
    pass