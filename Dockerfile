FROM python:3.9

WORKDIR /python-websocket

RUN pip install --upgrade pip
RUN pip install aiohttp aiortc websockets

COPY ./ ./

WORKDIR /python-websocket/src

EXPOSE 8080

CMD ["python3", "main.py"]
