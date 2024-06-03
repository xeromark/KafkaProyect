from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from kafka import KafkaConsumer
import smtplib
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
        print("Texto agregado correctamente a metricas.txt")
    except Exception as e:
        print("Error al agregar texto a metricas.txt:", e)


def EnviarCorreo(mensaje):    # Configuración del servidor SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    gmail_user = "omarjavi03@gmail.com"
    gmail_password = "soke stll qbws nlmx"

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = "omarjavi03@gmail.com"
    msg['Subject'] = "Pedidos Universidad Deigo Morales"
    body = "Su pedido " + str(mensaje["id"]) + " de nombre " + mensaje["nombre"] + " de un monto de " + str(mensaje["precio"]) + " esta en estado: " + mensaje["estado"]

    # Adjuntar el cuerpo del mensaje al contenedor de MIME
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Iniciar sesión en el servidor SMTP y enviar el correo
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Iniciar la conexión TLS
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(gmail_user, "omar.marca@mail.udp.cl", text)
        server.quit()

        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar correo: {e}")



for mensaje in consumer:
    data = json.loads(mensaje.value.decode('utf-8')) #Pasamos el mensaje a un diccionario
    EnviarCorreo(data)
    agregar_a_metricas( str(data["meta"]) + "|" + str(time.time() - data["te"]))
    print( json.dumps(data) + " Delay: " + str(time.time() - data["te"]))





