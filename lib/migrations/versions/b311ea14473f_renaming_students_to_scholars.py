"""Renaming students to scholars

Revision ID: b311ea14473f
Revises: 791279dd0760
Create Date: 2023-12-07 13:20:16.955241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b311ea14473f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
