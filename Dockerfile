FROM python:3.11-slim

RUN apt-get update && apt-get install -y tor proxychains4 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN ls -la /app

RUN echo "socks5 127.0.0.1 9050" >> /etc/proxychains4.conf

CMD tor & sleep 15 && proxychains4 python3 app.py
