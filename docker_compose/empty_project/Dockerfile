FROM python:3.12

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'
ENV SECRET_LEY 'django-insecure-eok!&=-4@mi=l=xni7^23ewfgCCCCrfrtgCCC&-5gq%6r&$-i&!(omlqs)23s-'
ENV DB_NAME 'movies_database'
ENV DB_USER 'app'
ENV DB_PASSWORD '123qwe'
ENV DB_HOST '172.27.0.2'
ENV DEBUG 'True'
ENV ADMIN_LOGIN 'admin'
ENV ADMIN_PASSWORD 'admin123z'
ENV DEBUG_TOOLBAR 'True'
ENV ALLOWED_HOSTS '127.0.0.1,'

COPY app/run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY app/uwsgi/uwsgi.ini uwsgi.ini

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY app/ .

ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]