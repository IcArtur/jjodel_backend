FROM debian:bullseye-slim AS base

EXPOSE 8001
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN useradd --create-home appuser
ARG DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN chown appuser:appuser /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        gettext-base \
        libgdk-pixbuf2.0-0 \
        libpangocairo-1.0-0 \
        libpq5 \
        libproj19 \
        libpython3.9 \
        python3-pip \
        tdsodbc \
        unixodbc-dev \
    && odbcinst -i -d -f /usr/share/tdsodbc/odbcinst.ini \
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
        python3-dev \
        ssh-client
COPY ./requirements/dev.txt requirements.txt
RUN pip3 install -r requirements.txt
USER appuser
COPY --chown=appuser . .
CMD python3 manage.py migrate --noinput && \
   python3 manage.py migrate --noinput --database=timescale && \
   python3 manage.py runserver 0:8000


FROM base AS prod
ENV DJANGO_CONFIGURATION=Production DJANGO_SECRET_KEY=changeme
COPY ./requirements/prod.txt requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        python3-dev \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove \
        build-essential \
        libpq-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*
COPY --chown=appuser . .
USER appuser
RUN python3 manage.py collectstatic --clear --noinput
CMD python3 manage.py migrate --noinput && \
    uwsgi uwsgiconf/docker.ini



