from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# Configuración del consumidor de Kafka
consumer = KafkaConsumer(
    'marvel_topic',
    'weather_topic',
    group_id='my_consumer_group',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=False
)



# Configuración de MongoDB
client = MongoClient('localhost', 27017)
db = client.data_pipeline
marvel_collection = db.marvel_data
marvel_collection.create_index('name', unique=True)
weather_collection = db.weather_data
weather_collection.create_index('state', unique=True)


# Consumir y almacenar mensajes en MongoDB
for message in consumer:
    topic = message.topic
    print(f"Recibido mensaje de {topic}")
    if topic == 'marvel_topic':
    # Extraer solo los datos necesarios
        try:
            characters = []
            for character in message.value['data']['results']:
                character_data = {
                    'name': character['name'],
                    'comics_count': character['comics']['available'],
                    'series_count': character['series']['available']
                }
                characters.append(character_data)
            
            # Almacenar en MongoDB
            marvel_collection.insert_many(characters)
            
            # Confirmar el offset manualmente después de procesar cada mensaje
            consumer.commit()

        except KeyError as e:
            print("Conde gay",e )
            continue
        except Exception as e:
            print("Documento duplicado, abortando insercion")
    
    elif topic == 'weather_topic':
        try:
            weather_data = {
                'state': message.value['name'],
                'temperature': message.value['main']['temp'],
                'timestamp': message.value['dt']                
            }
            weather_collection.insert_one(weather_data)
            consumer.commit()
        except KeyError as e:
            print("error general", e)
        except Exception as e:
            print("Documento duplicado, abortando insercion")


