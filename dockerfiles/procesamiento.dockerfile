FROM python:latest
RUN pip3 install -r requirementos.txt
CMD ["python", "-u", "producer-consumer.py"] #Importante colocar -u para ue se puedan apreciar los logs en python