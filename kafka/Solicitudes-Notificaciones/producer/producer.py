from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json

app = Flask(__name__)

@app.route("/data/all", methods=['GET'])
def get_all_pedidos():
    data = request.get_data().decode("utf-8")
    print(data)
    
#producer = KafkaProducer(bootstrap_servers='localhost:9092')

def ParseToJson(linea):     # Estructura el string como un json, retorna un string con formato json
    elementos = linea.rstrip().split("|")
    
    data = {
        'nombre': elementos[0],
        'precio': elementos[1]
    }
    

    return json.dumps(data)


def extraerDatos():
    # Abre el archivo en modo lectura
    with open('pedidos', 'r') as archivo:
        # Lee cada línea del archivo e imprímela
        c = 0
        for linea in archivo:
            if c<1:
                producer.send('pedidos', ParseToJson(linea).encode('utf-8'))
                producer.flush()
                c+=1
            else:
                break
#extraerDatos()


get_all_pedidos()