from kafka import KafkaConsumer

consumer = KafkaConsumer('finalizados',
                         group_id='my-group',
                         bootstrap_servers=['172.16.0.20:9092'])


for mensaje in consumer:
    print(mensaje.value.decode('utf-8'))





