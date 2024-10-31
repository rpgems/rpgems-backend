"""add character table

Revision ID: 6e58e0af69d6
Revises: daa100588d00
Create Date: 2024-10-30 22:57:02.378133

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '6e58e0af69d6'
down_revision: Union[str, None] = 'daa100588d00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE character (
            id SERIAL PRIMARY KEY,
            uuid uuid DEFAULT uuid_generate_v4(),
            created_at timestamp with time zone DEFAULT current_timestamp,
            updated_at timestamp with time zone,
            is_deleted boolean DEFAULT false,
            name VARCHAR(40) NOT NULL,
            description VARCHAR(100) NOT NULL,
            class uuid REFERENCES character_class (uuid),
            experience_points INTEGER NOT NULL
        );
        """
    )

    op.execute(
        """
        CREATE UNIQUE INDEX idx_character_uuid ON character (uuid);
        """
    )

    op.execute(
        """
        CREATE TRIGGER update_character_updated_at BEFORE UPDATE
        ON character FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS update_character_updated_at ON character;")
    op.execute("DROP TABLE character;")
    op.execute("DROP INDEX IF EXISTS idx_character_uuid;")
