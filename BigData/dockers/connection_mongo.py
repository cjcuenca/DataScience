# Instalación de librería: pip install pymongo
import pymongo

# conexión a base de datos
cliente = pymongo.MongoClient("localhost", 27017)

db = cliente.test

#print(db)

def mostrar(db):
    datos = db.user.find({})
    for dato in datos:
        print(dato)

def insertDocument(db):
    db.user.insert_one({"name": "Carlos ", "age": 324})

# insertDocument(db)
# mostrar(db)

def actualizar(db):
    datos = db.user.find({})
    for dato in datos:
        if dato["name"] == 'Raul':
            # print(dato["_id"])
            idMongo = dato["_id"]
            db.user.update_one({"_id": idMongo}, {"$set":{"age": 78}})

# actualizar(db)

def delete(db):
    datos = db.user.find({})
    for dato in datos:
        if dato["name"] == 'Raul':
            # print(dato["_id"])
            idMongo = dato["_id"]
            db.user.delete_one({"_id": idMongo})

# delete(db)
# mostrar(db)