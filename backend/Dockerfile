FROM python:3.5.7
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN chmod +x /code/docker-entrypoint.sh
ENTRYPOINT ["/code/docker-entrypoint.sh"]