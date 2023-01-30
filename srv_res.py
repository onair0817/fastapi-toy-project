from fastapi import FastAPI
import json
import pika
import asyncio

app = FastAPI()


async def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(f"Received request: {json.loads(body)}")


@app.get("/")
async def read_root():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="hello")
    channel.basic_consume(callback, queue="hello", no_ack=True)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    await asyncio.get_event_loop().run_in_executor(None, channel.start_consuming)
