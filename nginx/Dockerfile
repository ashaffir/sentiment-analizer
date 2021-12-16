FROM nginx:1.19-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
# RUN mkdir /etc/nginx/conf.d/certs/
# COPY ./config/localhost.*  /etc/nginx/conf.d/certs/