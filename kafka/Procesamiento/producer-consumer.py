from kafka import KafkaProducer, KafkaConsumer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='kafka:9092')

consumer = KafkaConsumer('pedidos',
                         group_id='my-group',
                         bootstrap_servers=['kafka:9092'])

numeropedidos=0

def CambiarEstado(mensaje): # Le agrega o cambia el estado del mensaje
    global numeropedidos

    data = json.loads(mensaje)
    
    if 'estado' in data:    
        if data['estado'] == 'Recibido':    # Si el estado es recibido, pongale Preparando
            data['estado'] = 'Preparando'
            data["te"] += random.randint(10, 20)
            #print(data)
            return json.dumps(data)

        elif data['estado'] == 'Preparando' and data["te"] <= time.time():    # Si el estado es Preparando, pongale Entregando
            data['estado'] = 'Entregando'
            data["te"] +=  random.randint(10, 20)
            #print(data)
            return json.dumps(data)

        elif data['estado'] == 'Entregando' and data["te"] <= time.time():    # Si el estado es Entregando, pongale Finalizado
            data['estado'] = 'Finalizado'
            data["meta"] = numeropedidos - 1 # Actualizar
            #print(data)
            return json.dumps(data)
    else:
        numeropedidos+=1
        data["estado"] = "Recibido" # De NO existir un estado, pongale recibido
        data["meta"] = 0 # Metadata para avisar cuantos pedidos se hicieron ,mas que todo para hacer las metricas

        #print(data)
    return json.dumps(data) #Retorna un string

for mensaje in consumer:
    data = CambiarEstado(mensaje.value.decode('utf-8')) # Se le pasa un string como parametro que agrega o cambia el estado del mensaje
    auxData = json.loads(data) # Auxiliar para data que se usa para que data siga siendo un string, mientras que aux es un json


    #time.sleep(1)

    if 'estado' in auxData:
        if auxData['estado'] != 'Finalizado':    # Si el estado es distinto de finalizado, devuelvalo a la cola
            producer.send('pedidos', data.encode('utf-8'))
        else:
            producer.send('finalizados', data.encode('utf-8')) # Los finalizados se vana otra cola de finalizados, esto con el fin de que no colapsar la cola del topico de pedidos

    
    producer.flush()


