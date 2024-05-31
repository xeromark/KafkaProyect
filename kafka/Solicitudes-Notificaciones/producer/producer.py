from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json

app = Flask(__name__)
@app.route("/")
def index():
    return "¡Bienvenido a la aplicación de pedidos!"

producer = KafkaProducer(bootstrap_servers='localhost:9092')

contador = 0

def ParseToJson(linea):     # Estructura el string como un json, retorna un string con formato json
    elementos = linea.rstrip().split("|")
    data = {}
    contador+=1
    data["id"] = contador
    data["nombre"] = elementos[0]
    data["precio"] = elementos[1]

    
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
    app.run(debug=True, port=5001)

    