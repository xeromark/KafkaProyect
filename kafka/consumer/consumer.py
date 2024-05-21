from aiokafka import AIOKafkaConsumer
import asyncio

async def consume():
    consumer = AIOKafkaConsumer(
        'pedidos', '__consumer_offsets',
        bootstrap_servers='localhost:9092')
    await consumer.start()
    try:
        
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        await consumer.stop()

asyncio.run(consume())