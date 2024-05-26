from flask import Flask, jsonify, request

app = Flask(__name__)

pedidos = []

@app.route("/")
def index():
    return "¡Bienvenido a la aplicación de pedidos!"



@app.route("/data", methods=['POST'])
def get_pedido():
    data = { "Nombre": "id_data1", "Precio": "Tilin"}

    return jsonify(data), 200



"""
@app.route("/data", methods = ['POST'])
def crear_pedido():
    data = request.get_data().decode("utf-8")
    #pedidos.append(data)
    
    return data, 201

@app.route("/data/all", methods=['GET'])
def get_all_pedidos():
    return pedidos, 200
"""

if __name__ == "__main__":
    app.run(debug=True, port=5001)

    