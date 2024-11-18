import pytest
from httpx import AsyncClient, ASGITransport
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND

from app.main import app
from tests.unit import override_db_repository, DatabaseResult


@pytest.mark.asyncio
async def test__create_new_character_class_works():
    character_class_created = {
        "uuid": "2f4e555f-ea88-4580-9d1d-83efa04e08fd",
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
        assert json_response["uuid"] == character_class_created["uuid"]
        assert json_response["name"] == character_class_created["name"]

    executed_sql_statement: str = mocked_db_repository.write.call_args.kwargs['stmt'].text
    expected_sql_statement = """ INSERT INTO character_class (
                    name
                ) VALUES (
                    :name
                )
                RETURNING *
                """

    assert expected_sql_statement.strip() == executed_sql_statement.strip()


@pytest.mark.asyncio
async def test__create_new_character_class_fails():
    character_class_created = {}

    mocked_db_repo = override_db_repository()
    mocked_db_repo.write.return_value = DatabaseResult(stored_data=character_class_created)

    create_character_class_request_with_error = {
        "name": "Failure"
    }
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(url="/class/", json=create_character_class_request_with_error)

        assert response.status_code == HTTP_400_BAD_REQUEST

        json_response = response.json()
        assert json_response['message'] == 'Unexpected error: Operation creation failed.'

    executed_sql_statement: str = mocked_db_repo.write.call_args.kwargs['stmt'].text
    expected_sql_statement = """ INSERT INTO character_class (
                    name
                ) VALUES (
                    :name
                )
                RETURNING *
                """

    assert expected_sql_statement.strip() == executed_sql_statement.strip()


@pytest.mark.asyncio
async def test__get_character_class_works():
    character_class_result = {
        "uuid": "2f4e555f-ea88-4580-9d1d-83efa04e08fd",
        "name": "Warrior",
    }

    mocked_db_repository = override_db_repository()
    mocked_db_repository.read.return_value = DatabaseResult(stored_data=character_class_result)

    character_class_uuid_request = "2f4e555f-ea88-4580-9d1d-83efa04e08fd"

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get(url=f"/class/{character_class_uuid_request}")

        assert response.status_code == HTTP_200_OK

        json_response = response.json()
        assert json_response["uuid"] == character_class_result["uuid"]
        assert json_response["name"] == character_class_result["name"]

    executed_sql_statement: str = mocked_db_repository.read.call_args.kwargs['stmt'].text
    expected_sql_statement = """
                SELECT * FROM character_class WHERE uuid::text = :uuid and is_deleted = FALSE
                """

    assert expected_sql_statement.strip() == executed_sql_statement.strip()


@pytest.mark.asyncio
async def test__get_character_class_fails():
    character_class_result = {}

    mocked_db_repository = override_db_repository()
    mocked_db_repository.read.return_value = DatabaseResult(stored_data=character_class_result)

    character_class_uuid_request = "2f4e555f-ea88-4580-9d1d-83efa04e08f0"

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get(url=f"/class/{character_class_uuid_request}")

        assert response.status_code == HTTP_404_NOT_FOUND

        json_response = response.json()
        assert json_response["message"] == "No entity found"

    executed_sql_statement: str = mocked_db_repository.read.call_args.kwargs['stmt'].text
    expected_sql_statement = """
                SELECT * FROM character_class WHERE uuid::text = :uuid and is_deleted = FALSE
                """

    assert expected_sql_statement.strip() == executed_sql_statement.strip()
