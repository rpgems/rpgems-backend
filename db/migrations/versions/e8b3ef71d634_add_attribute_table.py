"""add attribute table

Revision ID: e8b3ef71d634
Revises: 8bb2b953e904
Create Date: 2024-10-30 22:33:59.298942

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'e8b3ef71d634'
down_revision: Union[str, None] = '8bb2b953e904'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE character_attribute (
            id SERIAL PRIMARY KEY,
            uuid uuid DEFAULT uuid_generate_v4(),
            created_at timestamp with time zone DEFAULT current_timestamp,
            updated_at timestamp with time zone,
            is_deleted boolean DEFAULT false,
            name VARCHAR(40) NOT NULL,
            description VARCHAR(100) NOT NULL,
            skill_points INTEGER NOT NULL
        );
        """
    )

    op.execute(
        """
        CREATE UNIQUE INDEX idx_character_attribute_uuid ON character_attribute (uuid);
        """
    )

    op.execute(
        """
        CREATE TRIGGER update_character_attribute_updated_at BEFORE UPDATE
        ON character_attribute FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS update_character_attribute_updated_at ON "
               "character_attribute;")
    op.execute("DROP TABLE character_attribute;")
    op.execute("DROP INDEX IF EXISTS idx_character_attribute_uuid;")
