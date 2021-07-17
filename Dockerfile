
FROM python:3.8.6-buster

COPY . .

COPY requirements.txt /requirements.txt

ADD credentials.json /credentials.json

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN export GOOGLE_APPLICATION_CREDENTIALS=credentials.json

ENV GOOGLE_APPLICATION_CREDENTIALS /credentials.json

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
