import requests

# URL de la API
url = 'https://fictional-garbanzo-7vvgj9jx5wq37j4-5001.app.github.dev/data'

# Datos que quieres enviar en la petición POST
data = 'Tuvieja|1234'

# Cabeceras, si son necesarias (por ejemplo, para autenticación o especificar el tipo de contenido)
headers = {
    'Content-Type': 'text/plain',  # Indicamos que los datos son texto plano
    'Authorization': 'Bearer tu_token'   # Si necesitas autenticación
}

with open('pedidos', 'r') as archivo:
    # Lee cada línea del archivo e imprímela
    c = 0
    for linea in archivo:
        response = requests.post(url, data=linea, headers=headers)
        #print(c)
        c+=1
"""
        # Comprobar el estado de la respuesta
        if response.status_code == 201:
            print('Petición exitosa')
            print('Respuesta:', response.text)
        else:
            print('Error en la petición:', response.status_code)
            print('Detalle:', response.text)
"""