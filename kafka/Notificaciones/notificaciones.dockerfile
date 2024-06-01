FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt primero
COPY requirements.txt /app/

# Instala las dependencias
RUN pip3 install -r requirements.txt

# Copia el resto de la aplicación
COPY . /app

# Configura el comando predeterminado para ejecutar el script producer.py
CMD ["python", "-u", "consumer.py"] #Importante colocar -u para ue se puedan apreciar los logs en python