"""add character_class table

Revision ID: 8bb2b953e904
Revises: 13a3febd670b
Create Date: 2024-10-28 19:36:50.362707

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '8bb2b953e904'
down_revision: Union[str, None] = '13a3febd670b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE character_class (
            id SERIAL PRIMARY KEY,
            uuid uuid DEFAULT uuid_generate_v4(),
            created_at timestamp with time zone DEFAULT current_timestamp,
            updated_at timestamp with time zone,
            is_deleted boolean DEFAULT false,
            name VARCHAR(40) NOT NULL
        );
        """
    )

    op.execute(
        """
        CREATE UNIQUE INDEX idx_character_class_uuid ON  character_class (uuid);
        """
    )

    op.execute(
        """
        CREATE TRIGGER update_character_class_updated_at BEFORE UPDATE
        ON character_class FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS update_character_class_updated ON character_class;")
    op.execute("DROP TABLE character_class;")
    op.execute("DROP INDEX IF EXISTS idx_character_class_uuid;")

