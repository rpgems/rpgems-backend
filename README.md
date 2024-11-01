# RPGems

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ced39e83468e4b37bacbcd45fc66a630)](https://app.codacy.com/gh/rpgems/rpgems-backend/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/ced39e83468e4b37bacbcd45fc66a630)](https://app.codacy.com/gh/rpgems/rpgems-backend/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

A system to create and play an RPG game

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

## Using docker to run the environment

In order to have our system running, we'll need the following requirements:

- a frontend application (at the moment we're using a nginx container as placeholder)
- a backend application
- a database instance (a postgresql db engine version 16.4)

We're going to use [Docker](https://www.docker.com/) to emulate our system in a local environment.
In order to use it, you'll need to have at least docker compose version `2.29.x`.

In a terminal, run the following command:

`docker-compose -f ./docker/docker-compose.yaml up`

This will pull and build all required containers.
After the command finishes its execution, you can access the fronted using the browser in the following address:

`http://localhost:8000`

If you need to access the backend rest API, you can access it using the following url:

`http://localhost`