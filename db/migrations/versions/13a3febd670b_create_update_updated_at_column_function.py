"""create update_updated_at_column function

Revision ID: 13a3febd670b
Revises: 8901a7c94ffa
Create Date: 2024-10-28 19:36:19.812476

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '13a3febd670b'
down_revision: Union[str, None] = '8901a7c94ffa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
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
    op.execute("DROP FUNCTION IF EXISTS update_updated_at_column;")