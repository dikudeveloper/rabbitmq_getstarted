# A Producer Application (Client) -- AMQP 0-9-1 -
# Sends messages to a Queue through an exchange

import pika


# Establish a connection to RabbitMQ server (Broker) and create a channel.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Create a Queue, <hello>, before sending any message
channel.queue_declare(queue='hello')


# Send a message through an Exchange (default exchange in this case):
# Specify the Queue, <hello>, and <body> of the message.
# Note: Messages cannot be sent directly to the Queue but only through an Exchange.

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")


# Before exiting the client program, we need to ensure the network buffers
# were flushed and the message delivered to RabbitMQ server.
# We do this by closing the connection.
# verify this on the server: /var/log/rabbitmq/rabbit*.log
connection.close()
