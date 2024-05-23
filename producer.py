import requests
import json
from kafka import KafkaProducer
import time
import hashlib
import os 
from dotenv import load_dotenv
# Configuración de las APIs
marvel_public_key = os.getenv('MARVEL_PUBLIC_KEY')
marvel_private_key = os.getenv('MARVEL_PRIVATE_KEY')
ts = str(time.time())
hash_string = f"{ts}{marvel_private_key}{marvel_public_key}"
hash_result = hashlib.md5(hash_string.encode()).hexdigest()

# Índice de la página actual para la API de Marvel
marvel_page = 0

# Configuración del productor de Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Función para obtener datos de Marvel
def get_marvel_data(page):
    # Ajustar la URL para incluir el índice de la página actual
    marvel_url = f"http://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={marvel_public_key}&hash={hash_result}&offset={page*20}"
    response = requests.get(marvel_url)
    return response.json()

# Publicar mensajes en Kafka
while True:
    # Obtener datos de Marvel para la página actual
    marvel_data = get_marvel_data(marvel_page)
    
    # Enviar datos de Marvel a Kafka
    producer.send('marvel_topic', value=marvel_data)
    
    # Incrementar el índice de la página para la próxima llamada
    marvel_page += 1
    
    time.sleep(60)  # Esperar un minuto antes de la próxima llamada
