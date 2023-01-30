from fastapi import FastAPI
import pika

app = FastAPI()

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    message = {"item_id": item_id}
    if q:
        message["q"] = q
    channel.basic_publish(exchange="", routing_key="task_queue", body=str(message))
    return {"item_id": item_id, "message": "Message sent to RabbitMQ"}
