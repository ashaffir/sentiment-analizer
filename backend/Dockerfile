###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.5-slim-buster as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
RUN pip install --upgrade pip
# RUN pip install flake8==3.9.1
COPY . /usr/src/app/
# RUN flake8 --ignore=E501,F401 .

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9.5-slim-buster

# create directory for the app user
RUN mkdir -p /home/app

# Create static and media areas
RUN mkdir -p /vol/web/static
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/logs

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME
RUN chown -R app:app /vol/web

# SSL
RUN mkdir -p /etc/certs
RUN mkdir -p /var/log/gunicorn
# COPY ../nginx/config/localhost.crt /etc/certs
# COPY ../nginx/config/localhost.key /etc/certs
RUN chown -R app:app /etc/certs
RUN chown -R app:app /var/log/gunicorn

# NLTK 
ENV NLTK_DATA=/usr/local/nltk_data

RUN [ "python", "-c", "import nltk; nltk.download('vader_lexicon', download_dir='/usr/local/nltk_data')" ]
RUN chown -R app:app /usr/local/nltk_data

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]