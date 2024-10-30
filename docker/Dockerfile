FROM python:3.11-alpine3.20

ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH=/rpgems/.venv/bin:$PATH

RUN apk add curl=8.10.1-r0

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /rpgems

COPY pyproject.toml /rpgems

RUN PATH=/root/.local/bin:$PATH poetry install

COPY app /rpgems/app/

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]