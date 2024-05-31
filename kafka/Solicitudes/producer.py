# fuente https://pypi.org/project/watchdog/
# https://stackoverflow.com/questions/32923451/how-to-run-an-function-when-anything-changes-in-a-dir-with-python-watchdog
import sys
import time
import logging
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if isinstance(event, FileModifiedEvent) and event.src_path.endswith("datos.json"):
            data = []
            nombre = ""
            precio = 0
            # data is a json file
            with open(event.src_path, "r") as file:
                try:
                    data = json.load(file)
                    if "id" not in data:
                        with open("counter.txt", "r") as file:
                            id = int(file.read())
                        id += 1
                        nombre = data["Nombre"]
                        precio = data["Precio"]
                        new_data = {
                            "id": id,
                            "Nombre": nombre,
                            "Precio": precio
                        }
                        with open("counter.txt", "w") as file:
                            file.write(str(id))
                        with open(event.src_path, "w") as file:
                            json.dump(new_data, file)
                        producer.send('pedidos', json.dumps(new_data).encode('utf-8'))
                        producer.flush()
                except:
                    print("No datos necesarios en archivo")

            print(f"Archivo modificado: {event.src_path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1/1000)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()




"""
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
"""