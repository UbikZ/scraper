"""Create FEED schema

Revision ID: 4bac76361689
Revises: 
Create Date: 2016-11-01 22:53:04.533653

"""
from alembic import op
import sqlalchemy as sa

revision = '4bac76361689'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('feed',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('label', sa.String(), nullable=False),
                    sa.Column('url', sa.String(), nullable=False),
                    sa.Column('is_enabled', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('feed')
