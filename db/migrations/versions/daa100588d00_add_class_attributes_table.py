"""add class_attributes table

Revision ID: daa100588d00
Revises: e8b3ef71d634
Create Date: 2024-10-30 22:45:30.601487

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'daa100588d00'
down_revision: Union[str, None] = 'e8b3ef71d634'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE class_attributes (
            id SERIAL PRIMARY KEY,
            created_at timestamp with time zone DEFAULT current_timestamp,
            updated_at timestamp with time zone,
            is_deleted boolean DEFAULT false,
            class_uuid uuid REFERENCES character_class (uuid),
            attribute_uuid uuid REFERENCES character_attribute (uuid)
        );
        """
    )

    op.execute(
        """
        CREATE UNIQUE INDEX idx_class_attribute_class_uuid ON class_attributes (class_uuid);
        """
    )

    op.execute(
        """
        CREATE TRIGGER update_class_attributes_updated_at BEFORE UPDATE
        ON class_attributes FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS update_class_attributes_updated_at ON "
               "class_attributes;")
    op.execute("DROP TABLE class_attributes;")
    op.execute("DROP INDEX IF EXISTS idx_class_attribute_class_uuid;")
