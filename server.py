from pydantic import BaseModel
from fastapi import FastAPI
import aio_pika
import aiohttp
import asyncio


app = FastAPI()


class Request(BaseModel):
    url: str
    params: dict


class Response(BaseModel):
    status_code: int
    content: dict


async def process_message(message: aio_pika.IncomingMessage):
    async with message.process():
        request_body = message.body.decode()
        request = Request(**request_body)
        response = await call_api_server(request)
        await publish_response(response)


"""
async def process_message(channel, method, properties, body):
    api_servers = [f"http://api-server-{i}.com" for i in range(1, 6)]
    request_data = json.loads(body)
    server_index = hash(request_data["user_id"]) % len(api_servers)
    server_url = api_servers[server_index]
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{server_url}/data", params=request_data) as resp:
            api_response = await resp.json()
    result = aggregate_results(api_response)
    await channel.basic_publish(
        exchange_name,
        routing_key="aggregated_result",
        properties=pika.BasicProperties(delivery_mode=2,),
        body=json.dumps(result),
    )
    await channel.basic_ack(delivery_tag=method.delivery_tag)
"""


async def call_api_server(request: Request):
    async with aiohttp.ClientSession() as session:
        async with session.post(request.url, json=request.params) as resp:
            api_response = await resp.json()
    return Response(status_code=resp.status, content=api_response)


async def publish_response(response: Response):
    # code to publish response to another queue
    pass


@app.post("/ingress")
async def ingress(request: Request):
    await publish_request(request)
    return {"message": "success"}


async def publish_request(request: Request):
    # code to publish request to a queue
    pass


async def main():
    # code to connect rabbitmq
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@localhost/", loop=asyncio.get_event_loop()
    )
    channel = await connection.channel()
    queue = await channel.declare_queue("request_queue", durable=True)
    await queue.consume(process_message)


if __name__ == "__main__":
    asyncio.run(main())
