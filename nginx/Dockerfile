FROM nginx:1.21-alpine

RUN apk update \
    && apk add vim
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d/
# RUN mkdir /etc/nginx/conf.d/certs/
# COPY ./config/localhost.*  /etc/nginx/conf.d/certs/