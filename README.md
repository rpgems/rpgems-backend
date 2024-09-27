# RPGems

A system to create and play a RPG game

## Environment Setup

In order to run locally this application, you'll need to install the following dependency:

 - [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

After you install `pyenv`, install Python version 3.11 to your environment, running the following command:

`pyenv install 3.11`

You'll need to install another dependency:

 - [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

After poetry is installed, run the following command:

`poetry install`

This will install all the dependencies listed in the poetry configuration [file](pyproject.toml).
To enter the development environment, execute the following command:

`poetry shell`

Now that your environment is set, you can run the following command:

`uvicorn app.main:app --host localhost --port 8080 --reload`

And go to the browser on the following [location](http://localhost:8080/docs).
There you can find a documentation for the available endpoints in a Swagger like format.