
from kafka import KafkaConsumer
import json
import time

consumer = KafkaConsumer('finalizados',
                         group_id='my-group',
                         bootstrap_servers=['kafka:9092'])

a = time.time()
def CalcularDelay():
    print("a")

for mensaje in consumer:
    data = json.loads(mensaje.value.decode('utf-8')) #Pasamos el mensaje a un diccionario
    print(json.dumps(data) +" Delay: " + str(time.time() - data["creacion"]))





