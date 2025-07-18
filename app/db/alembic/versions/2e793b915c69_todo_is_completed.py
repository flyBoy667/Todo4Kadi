"""Todo is_completed

Revision ID: 2e793b915c69
Revises: 590dcb069831
Create Date: 2025-07-14 11:44:37.145420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e793b915c69'
down_revision: Union[str, Sequence[str], None] = '590dcb069831'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('is_completed', sa.Boolean(), nullable=False))
    op.drop_column('todos', 'status')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('todos', 'is_completed')
    # ### end Alembic commands ###
