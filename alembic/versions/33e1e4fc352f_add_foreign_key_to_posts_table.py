"""add foreign key to posts table

Revision ID: 33e1e4fc352f
Revises: 9a549a16f4bd
Create Date: 2022-10-10 22:40:23.468744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33e1e4fc352f'
down_revision = '9a549a16f4bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table = "posts", referent_table="users", local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name = "posts")
    op.drop_column('posts', 'ownner_id')
    pass
