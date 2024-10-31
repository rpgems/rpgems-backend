"""add character_attributes table

Revision ID: ebfd203b01d0
Revises: 6e58e0af69d6
Create Date: 2024-10-30 23:03:02.528602

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'ebfd203b01d0'
down_revision: Union[str, None] = '6e58e0af69d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE character_attributes (
            id SERIAL PRIMARY KEY,
            created_at timestamp with time zone DEFAULT current_timestamp,
            updated_at timestamp with time zone,
            is_deleted boolean DEFAULT false,
            character_uuid uuid REFERENCES character (uuid),
            attribute_uuid uuid REFERENCES character_attribute (uuid)
        );
        """
    )

    op.execute(
        """
        CREATE UNIQUE INDEX idx_character_attributes_character_uuid ON character_attributes (
        character_uuid);
        """
    )

    op.execute(
        """
        CREATE TRIGGER update_character_attributes_updated_at BEFORE UPDATE
        ON character_attributes FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS update_character_attributes_updated_at ON "
               "character_attributes;")
    op.execute("DROP TABLE character_attributes;")
    op.execute("DROP INDEX IF EXISTS idx_character_attributes_character_uuid;")
