import pytest

from app.adapters.repositories.characters.character_class_repository import CharacterClassRepository
from app.adapters.repositories.characters.schemas import CharacterClassCreate
from app.domain.character_class import CharacterClass


@pytest.mark.asyncio
async def test__save_new_character_class(
        character_class_repository: CharacterClassRepository,
):
    saved_char_class = await character_class_repository.save(
        CharacterClassCreate(name="Warrior")
    )

    assert isinstance(saved_char_class, CharacterClass)
    assert saved_char_class.id is not None
    assert saved_char_class.name == "Warrior"
