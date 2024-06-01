FROM python:latest
EXPOSE 5001
RUN ls
# RUN pip3 install -r requerimientos.txt
CMD ["python", "-u", "producer.py"] #Importante colocar -u para ue se puedan apreciar los logs en python