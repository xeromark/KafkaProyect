from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('pedidos', b'some_message_bytes')
producer.flush()


def extraerDatos():
    # Abre el archivo en modo lectura
    with open('pedidos', 'r') as archivo:
        # Lee cada línea del archivo e imprímela
        for linea in archivo:
            asyncio.run(send_one(linea))
