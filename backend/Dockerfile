FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'backend.settings'

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip && pip install -r requirements.txt

COPY backend .

EXPOSE 8000

ENTRYPOINT ["gunicorn", "backend.wsgi"]
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi", "--reload"]
