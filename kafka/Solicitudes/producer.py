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

producer = KafkaProducer(bootstrap_servers='172.16.0.20:9092') # Arreglar!
# Check if buffer.txt exists

    
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

    
    return json.dumps(data)




@app.route("/data", methods = ['POST'])
def crear_pedido():

    data = request.get_data().decode("utf-8") # Pasamos el archivo a texto plano

    producer.send('pedidos', ParseToJson(data).encode('utf-8')) # Envia la informacion
    producer.flush()
    return data, 201






def extraerDatos():
    # Abre el archivo en modo lectura
    with open('pedidos', 'r') as archivo:
        # Lee cada línea del archivo e imprímela
        c = 0
        for linea in archivo:
            if c<2:
                producer.send('pedidos', ParseToJson(linea).encode('utf-8'))
                producer.flush()
                c+=1
            else:
                break
#extraerDatos()

if __name__ == "__main__":
    app.run(debug=True, port=5001, host='172.16.0.12')
    with open('buffer.txt', 'w') as file:
        file.write('0')

    