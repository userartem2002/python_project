FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /home/test/PycharmProjects/pythonProject123/mysite
WORKDIR /home/test/PycharmProjects/pythonProject123/mysite



#RUN pip install gunicorn
#RUN apt-get install python-dev libxml2-dev libxslt-dev libpq-dev gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN flake8 --exit-zero mysite/proj/views.py && bandit --exit-zero mysite/proj/views.py
#RUN python mysite/te.py

CMD ["python" , "mysite/manage.py",  "runserver" , ";" , "python" ,  "mysite/te.py"]
