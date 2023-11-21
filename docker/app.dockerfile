ARG REGISTRY=""

FROM ${REGISTRY}python:3.11-slim

WORKDIR /app/

COPY ./requirements.txt /tmp

RUN python -m pip install --upgrade pip  \
    && python -m pip install pip-tools \
    && pip-sync /tmp/requirements.txt

# Build directory structure
COPY ./app /app/app
COPY ./alembic.ini /app
COPY ./alembic /app/alembic

# Add trampoline
COPY ./app/start.sh /start.sh
RUN chmod +x /start.sh

ENV PYTHONPATH=/app
