FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /home/test/PycharmProjects/pythonProject123/mysite
WORKDIR /home/test/PycharmProjects/pythonProject123/mysite

RUN pip install --upgrade pip
#RUN pip install gunicorn
#RUN apt-get install python-dev libxml2-dev libxslt-dev libpq-dev gcc

RUN pip install -r requirements.txt

RUN python -m pip install django

CMD python mysite/manage.py runserver
