"""add uuid generator extension

Revision ID: 8901a7c94ffa
Revises: 
Create Date: 2024-10-24 23:29:47.705464

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8901a7c94ffa"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    op.execute('SET TIME ZONE "UTC";')
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
        NEW.updated_at = current_timestamp;
        RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        """
    )


def downgrade() -> None:
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp";')
    op.execute("DROP FUNCTION update_updated_at_column() CASCADE;")
