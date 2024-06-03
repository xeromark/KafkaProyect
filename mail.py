import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP de Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587
gmail_user = "omarjavi03@gmail.com"
gmail_password = ""

# Crear el mensaje
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = "omarjavi03@gmail.com"
msg['Subject'] = "Asunto del correo"
body = "Este es el cuerpo del correo."

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
