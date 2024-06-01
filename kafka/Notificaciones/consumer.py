
from kafka import KafkaConsumer

consumer = KafkaConsumer('finalizados',
                         group_id='my-group',
                         bootstrap_servers=['kafka:9092'])


for mensaje in consumer:
    print(mensaje.value.decode('utf-8'))




print("hello")
