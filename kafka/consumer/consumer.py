from kafka import KafkaConsumer
import asyncio

consumer = KafkaConsumer('pedidos',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    print(message)


