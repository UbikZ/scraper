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
        CREATE OR REPLACE FUNCTION public.sp_edit_feed(
            v_ref_key VARCHAR,
            v_url VARCHAR,
            v_is_enabled BOOLEAN
        ) RETURNS integer
        AS $function$
          DECLARE
            result INTEGER;
          BEGIN
            INSERT INTO feed (ref_key, url, is_enabled) VALUES (v_ref_key, v_url, v_is_enabled)
              ON CONFLICT
              ON CONSTRAINT "c_unique_feed_refKey"
              DO UPDATE SET
                url = ISNULL(v_url, url),
                is_enabled = ISNULL(v_is_enabled, is_enabled)
              RETURNING id INTO result;
            RETURN result;
          END;
        $function$
        LANGUAGE plpgsql
    """)

    # Create or update feed type
    op.execute("""
            CREATE OR REPLACE FUNCTION public.sp_edit_feedType(
                v_ref_key VARCHAR,
                v_label VARCHAR,
                v_url_regexp VARCHAR,
                v_content_regexp VARCHAR,
                v_is_enabled BOOLEAN
            ) RETURNS integer
            AS $function$
              DECLARE
                result INTEGER;
              BEGIN
                INSERT INTO feed (ref_key, url, is_enabled) VALUES (v_ref_key, v_url, v_is_enabled)
                  ON CONFLICT
                  ON CONSTRAINT "c_unique_feedType_refKey"
                  DO UPDATE SET
                    url = ISNULL(v_url, url),
                    is_enabled = ISNULL(v_is_enabled, is_enabled)
                  RETURNING id INTO result;
                RETURN result;
              END;
            $function$
            LANGUAGE plpgsql
        """)

    # Create or update feed item
    op.execute("""
        CREATE OR REPLACE FUNCTION public.sp_edit_feedItem(
            v_id INTEGER,
            v_feed_id INTEGER,
            v_feed_type INTEGER,
            v_url VARCHAR,
            v_hash VARCHAR,
            v_title VARCHAR,
            v_tags VARCHAR,
            v_date TIMESTAMP,
            v_is_enabled BOOLEAN,
            v_is_viewed BOOLEAN,
            v_is_approved BOOLEAN,
            v_is_reposted BOOLEAN,
            v_is_sent BOOLEAN
        ) RETURNS integer
        AS $function$
          DECLARE
            result INTEGER;
          BEGIN
            INSERT INTO feed (hash, feed_id, feed_type, url, title, tags, "date", is_enabled, is_viewed, is_approved, is_reposted, is_sent)
            VALUES (v_hash, v_feed_id, v_feed_type, v_url, v_title, v_tags, v_date, v_is_enabled, v_is_viewed, v_is_approved, v_is_reposted, v_is_sent)
              ON CONFLICT
              ON CONSTRAINT "c_unique_feedItem_hash"
              DO UPDATE SET
                feed_id = ISNULL(v_feed_id, feed_id),
                feed_type = ISNULL(v_feed_type, feed_type),
                url = ISNULL(v_url, url),
                title = ISNULL(v_title, title),
                tags = ISNULL(v_tags, tags),
                "date" = ISNULL(v_date, "date"),
                is_enabled = ISNULL(v_is_enabled, is_enabled),
                is_viewed = ISNULL(v_is_viewed, is_viewed),
                is_approved = ISNULL(v_is_approved, is_viewed),
                is_respoted = ISNULL(v_is_reposted, is_reposted),
                is_sent = ISNULL(v_is_sent, is_sent)
              RETURNING id INTO result;
            RETURN result;
          END;
        $function$
        LANGUAGE plpgsql
    """)

    op.execute("""
      CREATE OR REPLACE FUNCTION public.sp_edit_user(
          v_username VARCHAR,
          v_email VARCHAR,
          v_token VARCHAR,
          v_is_enabled BOOLEAN
      ) RETURNS integer
      AS $function$
        DECLARE
          result INTEGER;
        BEGIN
          INSERT INTO feed (username, email, token, is_enabled)
          VALUES (v_username, v_email, v_token, v_is_enabled)
            ON CONFLICT
            ON CONSTRAINT "c_unique_user_username"
            DO UPDATE SET
              email = ISNULL(v_email, email),
              token = ISNULL(v_token, token),
              is_enabled = ISNULL(v_is_enabled, is_enabled)
            RETURNING id INTO result;
          RETURN result;
        END;
      $function$
      LANGUAGE plpgsql
    """)

    pass


def downgrade():
    op.execute("""
        DROP FUNCTION sp_edit_feed(VARCHAR, VARCHAR, BOOLEAN);
    """)
    pass
