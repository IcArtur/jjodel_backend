FROM python:3.8-slim-buster AS base

EXPOSE 8000

RUN useradd --create-home appuser

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 DEBIAN_FRONTEND=noninteractive


WORKDIR /app

RUN chown appuser:appuser /
RUN chown appuser:appuser /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        gettext \
        libpq5 \
        libcairo2 \
        libpango1.0-0 \
        mime-support \
        gdal-bin \
    && rm -rf /var/lib/apt/lists/*

FROM base AS test

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && pip3 install --no-cache-dir -U pip tox
CMD tox -e coverage,reporthtml,report


FROM base AS dev
ENV PRE_COMMIT_HOME=/app/.cache/.pre-commit
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        libpq-dev \
        make \
        ssh-client
COPY ./requirements/dev.txt requirements.txt
RUN pip3 install -r requirements.txt
USER appuser
COPY --chown=appuser . .
CMD python manage.py migrate --noinput && \
   python manage.py runserver 0:8000


FROM base AS prod
ENV DJANGO_CONFIGURATION=Production DJANGO_SECRET_KEY=changeme
COPY ./requirements/prod.txt requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*
COPY --chown=appuser . .
USER appuser
RUN python manage.py collectstatic --clear --noinput
CMD python manage.py migrate --noinput && \
    uwsgi uwsgiconf/docker.ini
