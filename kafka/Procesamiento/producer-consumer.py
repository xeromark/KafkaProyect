from kafka import KafkaProducer, KafkaConsumer
import json
import time

producer = KafkaProducer(bootstrap_servers='kafka:9092')

consumer = KafkaConsumer('pedidos',
                         group_id='my-group',
                         bootstrap_servers=['kafka:9092'])


def AgregarEstado(mensaje): # Le agrega o cambia el estado del mensaje
    data = json.loads(mensaje)
    
    if 'estado' in data:    # Si existe un estado, pongale finalizado
        if data['estado'] == 'Recibido':
            data['estado'] = 'Finalizado'
            return json.dumps(data)
        
    data["estado"] = "Recibido" # De NO existir un estado, pongale recibido
        

    return json.dumps(data) #Retorna un string

for mensaje in consumer:
    data = AgregarEstado(mensaje.value.decode('utf-8')) # Se le pasa un string como parametro que agrega o cambia el estado del mensaje
    auxData = json.loads(data) # Auxiliar para data que se usa para que data siga siendo un string, mientras que aux es un json
    print(data)
    #time.sleep(1)

    if 'estado' in auxData:
        if auxData['estado'] == 'Recibido':    # Los recibidos se van devuelta a la cola de los pedidos
            producer.send('pedidos', data.encode('utf-8'))
        else:
            producer.send('finalizados', data.encode('utf-8')) # Los finalizados se vana otra cola de finalizados, esto con el fin de que no colapsar la cola del topico de pedidos

    
    producer.flush()


