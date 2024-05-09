FROM python:3.12
ENV PYTHONUNBUFFERED 1
WORKDIR /app
# Instala las dependencias del sistema necesarias, incluyendo libpq-dev para psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/

CMD python manage.py runserver 0.0.0.0:8000