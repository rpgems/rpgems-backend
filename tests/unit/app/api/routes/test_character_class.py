import pytest
from httpx import AsyncClient, ASGITransport
from starlette.status import HTTP_201_CREATED

from app.main import app
from tests.unit import override_db_repository, DatabaseResult


@pytest.mark.asyncio
async def test__create_new_character_class_works():
    character_class_created = {
        "id": 1,
        "name": "Warrior",
    }

    mocked_db_repository = override_db_repository()
    mocked_db_repository.write.return_value = DatabaseResult(stored_data=character_class_created)

    create_character_class_request = {
        "name": "Warrior"
    }
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(url="/class/", json=create_character_class_request)

        assert response.status_code == HTTP_201_CREATED

        json_response = response.json()
        assert json_response["id"] == character_class_created["id"]
        assert json_response["name"] == character_class_created["name"]
        assert json_response["attributes"] == []

    executed_sql_statement: str = mocked_db_repository.write.call_args.kwargs['stmt'].text
    expected_sql_statement =""" INSERT INTO character_class (
                    name
                ) VALUES (
                    :name,
                )
                RETURNING *
                """

    assert expected_sql_statement.strip() == executed_sql_statement.strip()
