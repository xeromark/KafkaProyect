
from kafka import KafkaConsumer
import json
import time

consumer = KafkaConsumer('finalizados',
                         group_id='my-group',
                         bootstrap_servers=['kafka:9092'])

def agregar_a_metricas(texto):
    try:
        # Abre el archivo en modo de escritura (append)
        with open("metricas.txt", "a") as archivo:
            # Escribe el texto en el archivo seguido de un salto de línea
            archivo.write(texto + "\n")
        #print("Texto agregado correctamente a metricas.txt")
    except Exception as e:
        print("Error al agregar texto a metricas.txt:", e)




for mensaje in consumer:
    data = json.loads(mensaje.value.decode('utf-8')) #Pasamos el mensaje a un diccionario
    agregar_a_metricas( str(data["meta"]) + "|" + str(time.time() - data["te"]))
    #print( json.dumps(data) + " Delay: " + str(time.time() - data["te"]))





