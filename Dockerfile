#https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
FROM python:3.9-slim

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN touch ./pickle-jar/last_tweet.pickle

COPY . .

RUN touch ./pickle-jar/last_tweet.pickle

CMD ["python", "./twitter_bot/main.py"]