# A Consumer Application (Client) -- AMQP 0-9-1
# Receives messages from a Queue:

import pika


# Establish a connection to RabbitMQ server (Broker) and create a channel.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Create a Queue, <hello>, before sending any message:
# Since we don't know if the Queue is already created, it is good practice to re-declare it.
# That's because we don't know if the Producer program has already run before the Consumer.
# Note: Re-declaring the Queue does not change it -- it can be done multiple times with no impact.
channel.queue_declare(queue='hello')


# Receiving messages from a queue works by subscribing a Callback function to the Queue.
# Whenever we receive a message, this function is called.
# In this case the function will print on the screen the contents of the message.
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# Tell RabbitMQ server about this specific 'callback' function that will receive messages from the <hello> Queue.
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)


# Finally, we enter a never-ending loop that waits for data and runs callbacks whenever necessary.
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()