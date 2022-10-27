# Instalación de librería: pip install pymongo
from asyncio.windows_events import NULL
import pymongo

from datetime import date
from datetime import datetime


def Fecha_actual():
    now = datetime.now()
    # fecha = now.strftime('%d/%m/%Y %H:%M:%S') 
    fecha = now
    return fecha

# DATOS A CARGAR
datos_BB =[
       {
        "nombre": "Pedro López", 
        "edad": 324,
        "email" : "pedro@fei.com",
        "nota": 5.2, 
        "fecha": NULL
        },
        {
        "nombre": "Julia García", 
        "edad": 22, 
        "email": "julia@fei.com", 
        "nota": 7.3, 
        "fecha": NULL
        },
        {
        "nombre": "Amparo Mayoral", 
        "edad": 28, 
        "email": "amparo@fei.com", 
        "nota": 8.4, 
        "fecha": NULL
        } ,
        {
        "nombre": "Juan Martinez", 
        "edad": 30, 
        "email": "juan@fei.com", 
        "nota": 6.8, 
        "fecha": NULL
        }
        ]
# print(datos_BB)

# conexión a base de datos
cliente = pymongo.MongoClient("localhost", 27017)
db = cliente.actividad


def mostrar(db):
    datos = db.notas.find({})
    for dato in datos:
        print(dato)

# def mostrar(db, nombre):
#     datos = db.notas.find({})
#     for dato in datos:
#         if dato["nombre"] == nombre:
#             print(dato)

def insertDocument(db):
    for i in range(len(datos_BB)):
        datos_BB[i]["fecha"]=Fecha_actual()
        db.notas.insert_one(datos_BB[i])

# insertDocument(db)
# mostrar(db)


def actualizar(db,nombre,nota_new):
    datos = db.notas.find({})
    for dato in datos:
        if dato["nombre"] == nombre:
            idMongo = dato["_id"]
            db.notas.update_one({"_id": idMongo}, {"$set":{"nota": nota_new, "fecha":Fecha_actual()}})

#actualizar(db,"Amparo Mayoral", 9.3)
#mostrar(db, "Amparo Mayoral")
# actualizar(db,"Juan Martinez", 7.2)
# mostrar(db, "Juan Martinez")
# mostrar(db)


def mostrar_notas(db, nota_inf, nota_sup):
    datos = db.notas.find({})
    for dato in datos:
        if dato["nota"]>=nota_inf and dato["nota"]<=nota_sup:
            print(dato)

# mostrar_notas(db, 7, 7.5)


def delete(db, nombre):
    datos = db.notas.find({})
    for dato in datos:
        if dato["nombre"] == nombre:
            # print(dato["_id"])
            idMongo = dato["_id"]
            db.notas.delete_one({"_id": idMongo})

# delete(db,"Pedro López")
# mostrar(db)