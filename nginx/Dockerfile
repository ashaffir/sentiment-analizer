FROM nginx:1.21-alpine

RUN apk update \
    && apk add vim
RUN rm /etc/nginx/conf.d/default.conf
# COPY ./config/nginx.conf /etc/nginx/conf.d/nginx.conf
RUN mkdir /etc/nginx/conf.d/certs/
COPY ./config/localhost.crt  /etc/nginx/conf.d/certs/localhost.crt
COPY ./config/localhost.key  /etc/nginx/conf.d/certs/localhost.key
COPY ./scripts/aliases.sh  /etc/nginx/conf.d/certs/aliases.sh