from flask import Flask, jsonify, request
from kafka import KafkaProducer
import time
import json
import os

if not os.path.exists('buffer.txt'):
    with open('buffer.txt', 'w') as file:
        file.write('0')

app = Flask(__name__)
@app.route("/")
def index():
    return "¡Bienvenido a la aplicación de pedidos!"

producer = KafkaProducer(bootstrap_servers='kafka:9092')

    
def ParseToJson(linea):     # Estructura el string como un json, retorna un string con formato json
    elementos = linea.rstrip().split("|")
    data = {}
    with open('buffer.txt', 'r') as file:
        id = int(file.read())
        id+=1
    with open('buffer.txt', 'w') as file:
        file.write(str(id))
    data["id"] = id
    data["nombre"] = elementos[0]
    data["precio"] = elementos[1]

    data["creacion"] = time.time()
    data["te"] = data["creacion"] # Se agrega su tiempo estimado de preparacion o entrega, te = tiempo estimado

    
    return json.dumps(data)




@app.route("/data", methods = ['POST'])
def crear_pedido():

    data = request.get_data().decode("utf-8") # Pasamos el archivo a texto plano
    contador = 0
    #while contador < 2000:
    producer.send('pedidos', ParseToJson(data).encode('utf-8')) # Envia la informacion
        #contador+=1
    
    producer.flush()
    return data, 201


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
    with open('buffer.txt', 'w') as file:
        file.write('0')

    