FROM python:3.12-slim as builder

RUN apt-get update \
    && pip install --upgrade pip

FROM python:3.12

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY --from=builder /usr/local/lib/python3.12/site-packages/ .
COPY app/run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY app/uwsgi/uwsgi.ini uwsgi.ini
COPY app/run_uwsgi.sh run_uwsgi.sh

RUN pip install --no-cache-dir -r requirements.txt \
     && mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/

COPY app/ .

