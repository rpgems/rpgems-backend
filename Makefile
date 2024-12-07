PACKAGE_NAME=app

# Execute pylint check ignoring some docstring validation
pylint-check:
	poetry run pylint $(PACKAGE_NAME) --disable=C0114,C0115,C0116

# Execute pylint check with docstrings validation
pylint-check-docs:
	poetry run pylint $(PACKAGE_NAME)

# Execute black formatter and pylint check
pylint-fix:
	poetry run black $(PACKAGE_NAME)
	poetry run pylint $(PACKAGE_NAME) --disable=C0114,C0115,C0116

# Execute alembic on database test
# db-test-upgrade:
    #docker compose exec -e APP_DB_HOST=$APP_DB_HOST -e APP_DB_PORT=$APP_DB_PORT rpgems-db poetry run alembic -x env=test upgrade head
#    docker compose exec rpgems-db poetry run alembic -x env_file=/docker/.env-test upgrade head
