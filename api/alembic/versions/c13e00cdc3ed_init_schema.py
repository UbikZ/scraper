"""Init schema

Revision ID: c13e00cdc3ed
Revises: 
Create Date: 2016-11-02 15:11:06.075683

"""
from alembic import op
import sqlalchemy as sa

revision = 'c13e00cdc3ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    upgrade_feed()
    upgrade_feed_type()
    upgrade_feed_user()
    upgrade_feed_item()


def upgrade_feed():
    op.create_table('feed',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('ref_key', sa.String(length=100), nullable=False, unique=True),
                    sa.Column('url', sa.String(length=255), nullable=False),
                    sa.Column('is_enabled', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.execute(
        """
        CREATE OR REPLACE
        FUNCTION sp_edit_feed(v_ref_key VARCHAR(100), v_url VARCHAR(255), v_is_enabled boolean)
            RETURNS INTEGER AS $$
            DECLARE
              result INTEGER;
            BEGIN
              INSERT INTO feed (ref_key, url, is_enabled) VALUES (v_ref_key, v_url, v_is_enabled)
               ON CONFLICT ON CONSTRAINT feed_ref_key_key
               DO UPDATE SET url = v_url, is_enabled = v_is_enabled RETURNING id INTO result;
              RETURN result;
            END;
        $$ LANGUAGE plpgsql;
        """
    )


def upgrade_feed_type():
    op.create_table('feed_type',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('label', sa.String(length=100), nullable=False),
                    sa.Column('url_regexp', sa.String(length=255), nullable=False),
                    sa.Column('content_regexp', sa.String(length=255), nullable=False),
                    sa.Column('is_enabled', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def upgrade_feed_user():
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=100), nullable=False),
                    sa.Column('token', sa.String(length=255), nullable=False),
                    sa.Column('is_enabled', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('username')
                    )


def upgrade_feed_item():
    op.create_table('feed_item',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('feed_id', sa.Integer(), nullable=True),
                    sa.Column('feed_type', sa.Integer(), nullable=True),
                    sa.Column('url', sa.String(length=255), nullable=False),
                    sa.Column('title', sa.String(length=100), nullable=False),
                    sa.Column('tags', sa.String(length=255), nullable=True),
                    sa.Column('date', sa.DateTime(), nullable=False),
                    sa.Column('is_enabled', sa.Boolean(), nullable=False),
                    sa.Column('is_viewed', sa.Boolean(), nullable=False),
                    sa.Column('is_approved', sa.Boolean(), nullable=False),
                    sa.Column('is_reposted', sa.Boolean(), nullable=False),
                    sa.Column('is_sent', sa.Boolean(), nullable=False),
                    sa.ForeignKeyConstraint(['feed_id'], ['feed.id'], name='fk_feedItem_parent_feedId'),
                    sa.ForeignKeyConstraint(['feed_type'], ['feed_type.id'], name='fk_feedItem_parent_feedType'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('url')
                    )


def downgrade():
    op.drop_table('feed_item')
    op.drop_table('user')
    op.drop_table('feed_type')
    op.drop_table('feed')
