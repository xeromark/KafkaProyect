FROM python:latest
RUN ls
# RUN pip3 install -r requerimientos.txt
CMD ["python", "-u", "producer-consumer.py"] #Importante colocar -u para ue se puedan apreciar los logs en python