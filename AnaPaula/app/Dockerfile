# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

ENV FLASK_APP = src/app.py

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]