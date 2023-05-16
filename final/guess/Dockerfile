FROM python:3.9-slim

WORKDIR /app

COPY main.py /app

RUN apt-get update && apt-get install -y socat

EXPOSE 6000

CMD socat TCP-LISTEN:6000,fork,reuseaddr EXEC:"python3 main.py",pty,stderr
