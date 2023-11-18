FROM python:3.10-slim

WORKDIR /app

ENV PYTHONBUFFERED=1

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root --only main

COPY ./autoru_catalog .