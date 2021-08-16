FROM python:3.9-alpine

WORKDIR app

COPY requirements.txt /app
COPY server /app

RUN pip install -r /app/requirements.txt

EXPOSE 80
ENTRYPOINT gunicorn -w 8 -b 0.0.0.0:80 server:app
