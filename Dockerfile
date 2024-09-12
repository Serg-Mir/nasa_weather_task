# syntax=docker/dockerfile:1
FROM python:3.11-slim-bullseye

WORKDIR /opt
ENV PYTHONPATH=/opt:/opt/nasa_weather_data

COPY requirements/requirements.txt.txt requirements.txt

RUN pip install -r requirements.txt

COPY nasa_weather_data /opt/nasa_weather_data

ENTRYPOINT ["python", "nasa_weather_data/main.py"]
