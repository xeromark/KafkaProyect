FROM python:alphine
COPY ./app /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r requirementos.txt
CMD ["python", "-u", "app.py"] #Importante colocar -u para ue se puedan apreciar los logs en python