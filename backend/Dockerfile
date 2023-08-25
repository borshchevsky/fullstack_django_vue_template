FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'main.settings'

COPY requirements.txt requirements.txt
COPY run.sh run.sh
COPY wait-for-it.sh wait-for-it.sh
RUN chmod +x run.sh
RUN chmod +x wait-for-it.sh
RUN pip install --upgrade pip && pip install -r requirements.txt

# ???????
COPY . .

EXPOSE 8000

ENTRYPOINT ["./run.sh"]
