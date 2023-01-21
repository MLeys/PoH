FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip3 install poetry
RUN poetry install --no-root

COPY . .
COPY ./pyproject.toml ./poetry.lock*  ./
RUN poetry export -f requirements.txt --output requirements.txt && pip install --no-cache-dir -r requirements.txt

ENV DJANGO_SETTINGS_MODULE "poh.settings"
ENV DJANGO_SECRET_KEY "this is a secret key for building purposes"

RUN poetry run python manage.py collectstatic --noinput

CMD poetry run daphne -b 0.0.0.0 -p 8080 poh.asgi:application