FROM python:3.11-slim

RUN apt-get update && apt-get install -y tor proxychains4 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pexpect colorama

RUN echo "socks5 127.0.0.1 9050" >> /etc/proxychains4.conf

CMD tor & sleep 15 && python3 -u app.py & python3 -u telegram_bot.py
