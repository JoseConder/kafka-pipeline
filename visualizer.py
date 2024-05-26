import matplotlib.pyplot as plt
from pymongo import MongoClient

# Conexión a la base de datos de MongoDB
client = MongoClient('localhost', 27017)
db = client.data_pipeline
marvel_collection = db.marvel_data
weather_collection = db.weather_data

# Obtener datos de la colección de Marvel
marvel_data = marvel_collection.find({}, {'name': 1, 'comics_count': 1, 'series_count': 1})

# Crear listas para almacenar los datos de Marvel
names = []
comics_counts = []
series_counts = []

# Iterar sobre los datos de Marvel y almacenarlos en las listas
for entry in marvel_data:
    names.append(entry['name'])
    comics_counts.append(entry['comics_count'])
    series_counts.append(entry['series_count'])

# Crear gráfico para los datos de Marvel
plt.figure(figsize=(10, 6))
plt.bar(names, comics_counts, color='blue', alpha=0.5, label='Comics Count')
plt.bar(names, series_counts, color='green', alpha=0.5, label='Series Count')
plt.xlabel('Character Name')
plt.ylabel('Count')
plt.title('Comics Count vs Series Count by Character')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()

# Obtener datos de la colección de Weather
weather_data = weather_collection.find({}, {'state': 1, 'temperature': 1})

# Crear listas para almacenar los datos de Weather
cities = []
temperatures = []

# Iterar sobre los datos de Weather y almacenarlos en las listas
for entry in weather_data:
    cities.append(entry['state'])
    temperatures.append(entry['temperature'])

# Crear gráfico para los datos de Weather
plt.figure(figsize=(10, 6))
plt.bar(cities, temperatures, color='orange', alpha=0.7)
plt.xlabel('State')
plt.ylabel('Temperature (K)')
plt.title('Temperature by State in Mexico')
plt.xticks(rotation=90)
plt.tight_layout()

# Mostrar ambos gráficos a la vez
plt.show()
