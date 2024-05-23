import matplotlib.pyplot as plt
from pymongo import MongoClient

# Conexión a la base de datos de MongoDB
client = MongoClient('localhost', 27017)
db = client.data_pipeline
collection = db.marvel_data  # Reemplaza 'your_collection_name' con el nombre de tu colección

# Obtener datos de la colección
data = collection.find({}, {'name': 1, 'comics_count': 1, 'series_count': 1})

# Crear listas para almacenar los datos
names = []
comics_counts = []
series_counts = []

# Iterar sobre los datos y almacenarlos en las listas
for entry in data:
    names.append(entry['name'])
    comics_counts.append(entry['comics_count'])
    series_counts.append(entry['series_count'])

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.bar(names, comics_counts, color='blue', alpha=0.5, label='Comics Count')
plt.bar(names, series_counts, color='green', alpha=0.5, label='Series Count')
plt.xlabel('Character Name')
plt.ylabel('Count')
plt.title('Comics Count vs Series Count by Character')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()
