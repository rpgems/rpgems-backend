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

