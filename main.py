from models import Request
from services import publish_request, process_message

from fastapi import FastAPI
import toml
import aio_pika
import asyncio


app = FastAPI()
config = toml.load("configs/config.toml")


@app.post("/ingress")
async def ingress(request: Request):
    await publish_request(request)
    return {"message": "success"}


async def main():
    # code to connect rabbitmq
    connection = await aio_pika.connect_robust(
        f"amqp://{config['rabbitmq']['username']}:{config['rabbitmq']['password']}@{config['rabbitmq']['host']}/",
        loop=asyncio.get_event_loop(),
    )
    channel = await connection.channel()
    queue = await channel.declare_queue(config["rabbitmq"]["queue_name"], durable=True)
    await queue.consume(process_message)


if __name__ == "__main__":
    asyncio.run(main())
