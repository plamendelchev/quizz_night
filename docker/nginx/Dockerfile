FROM nginx:1.17

WORKDIR /etc/nginx

RUN rm conf.d/default.conf
COPY ./default.conf conf.d/

EXPOSE 80
