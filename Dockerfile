FROM python:3.12.0-alpine

RUN apk update

RUN mkdir /app
WORKDIR /app
COPY bot.py /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]