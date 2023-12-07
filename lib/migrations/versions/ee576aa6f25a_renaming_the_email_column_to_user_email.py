"""Renaming the email column to user_email

Revision ID: ee576aa6f25a
Revises: b311ea14473f
Create Date: 2023-12-07 14:32:48.719663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee576aa6f25a'
down_revision = 'b311ea14473f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('email', 'user_email')
    
    pass


def downgrade() -> None:
    op.alter_column('user_email','email')
    pass
