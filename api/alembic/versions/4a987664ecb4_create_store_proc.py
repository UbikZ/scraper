"""Create store proc

Revision ID: 4a987664ecb4
Revises: 
Create Date: 2016-11-11 17:10:19.117420

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4a987664ecb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create or update feed
    op.execute("""
        CREATE OR REPLACE FUNCTION public.sp_edit_feed(v_ref_key character varying, v_url character varying, v_is_enabled boolean)
         RETURNS integer
         LANGUAGE plpgsql
        AS $$
                    DECLARE
                      result INTEGER;
                    BEGIN
                      INSERT INTO feed (ref_key, url, is_enabled) VALUES (v_ref_key, v_url, v_is_enabled)
                       ON CONFLICT ON CONSTRAINT "c_unique_feed_refKey"
                         DO UPDATE SET url = v_url, is_enabled = v_is_enabled RETURNING id INTO result;
                      RETURN result;
                    END;
        $$
    """)
    pass


def downgrade():
    op.execute("""
        DROP FUNCTION sp_edit_feed(VARCHAR, VARCHAR, BOOLEAN);
    """)
    pass
