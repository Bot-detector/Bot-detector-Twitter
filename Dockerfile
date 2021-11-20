#https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
FROM python:3.9-slim

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "twitter_bot.main.py"]
