FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]