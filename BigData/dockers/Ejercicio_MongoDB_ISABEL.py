# Instalación de librería: pip install pymongo
import pymongo
from datetime import datetime

# fecha ejercicio
# fecha = datetime.strptime("12-11-2021 12:45:26", "%d-%m-%Y %H:%M:%S")

# Fecha actual
fecha = datetime.now()

# conexión a base de datos
cliente = pymongo.MongoClient("localhost", 27017)

db = cliente.actividad

# print(db)

data = [{"nombre": "Pedro López", "edad": 25, "email": "pedro@fei.com", "nota": 5.2, "fecha": fecha},
        {"nombre": "Julia García", "edad": 22, "email": "julia@fei.com", "nota": 7.3, "fecha": fecha},
        {"nombre": "Amparo Mayoral", "edad": 28, "email": "amparo@fei.com", "nota": 8.4, "fecha": fecha},
        {"nombre": "Juan Martínez", "edad": 30, "email": "juan@fei.com", "nota": 6.8, "fecha": fecha},]
# print(data)

def mostrar(db, colec):
    datos = db[colec].find({})
    for dato in datos:
        print(dato)

def insertDocument(db, colec, data):
    db[colec].insert_many(data)

# insertDocument(db, "notas", data)
# mostrar(db, "notas")

def actualizar(db, colec, name, nota):
    datos = db[colec].find({})
    for dato in datos:
        if dato["nombre"] == name:
            idMongo = dato["_id"]
            db[colec].update_one({"_id": idMongo}, {"$set":{"nota": nota}})

# actualizar(db, "notas", "Amparo Mayoral", 9.3)
# actualizar(db, "notas", "Juan Martínez", 7.2)
# mostrar(db, "notas")

def filtrar(db, colec, nota1, nota2):
    datos = db[colec].find({"$and": [{"nota": {"$gte": nota1}}, {"nota": {"$lte": nota2}}]},{})
    for dato in datos:
        print(dato)

# filtrar(db, "notas", 7, 7.5)

def delete(db, colec, name):
    datos = db[colec].find({})
    for dato in datos:
        if dato["nombre"] == name:
            idMongo = dato["_id"]
            db[colec].delete_one({"_id": idMongo})

# delete(db, "notas", "Pedro López")
# mostrar(db, "notas")