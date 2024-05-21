from flask import Flask, jsonify, request
from aiokafka import AIOKafkaProducer
import asyncio
import requests
import json



async def send_one(mensaje):
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092')
    await producer.start()
    try:
        await producer.send_and_wait("pedidos", mensaje.encode())
    finally:
        await producer.stop()




def extraerDatos():
    # Abre el archivo en modo lectura
    with open('pedidos', 'r') as archivo:
        # Lee cada línea del archivo e imprímela
        for linea in archivo:
            asyncio.run(send_one(linea))
extraerDatos()