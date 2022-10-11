"""add content column to posts table

Revision ID: 38c07531562d
Revises: 9ea08918b4c9
Create Date: 2022-10-10 00:57:46.371026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38c07531562d'
down_revision = '9ea08918b4c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
