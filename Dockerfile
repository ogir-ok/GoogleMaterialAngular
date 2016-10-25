FROM python:2.7
ENV PYTHONUNBUFFERED 1
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

