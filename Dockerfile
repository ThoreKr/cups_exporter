FROM python:3-alpine

ENV CUPS_HOST "127.0.0.1"
ENV CUPS_PORT "631"
ENV CUPS_USER "default"
ENV LISTEN_PORT "9329"

ADD . /opt/cups-exporter

WORKDIR /opt/cups-exporter

EXPOSE 9329

RUN set -xe;\
  apk add gcc libc-dev cups-dev;\
  pip install prometheus-client~=0.7.1 pycups~=1.9.74

CMD [ "sh", "-c", "./cups_exporter.py --cups-host ${CUPS_HOST} --cups-port ${CUPS_PORT} --cups-user ${CUPS_USER} --listen-port ${LISTEN_PORT}" ]
