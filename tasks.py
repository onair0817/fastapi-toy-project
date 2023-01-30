import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue="task_queue", durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue="task_queue", auto_ack=True, on_message_callback=callback)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
