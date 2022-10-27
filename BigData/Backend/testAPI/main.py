from fastapi import FastAPI, status, Response
# import pandas as pd 
# import json
# import csv
# import os

from pydantic import BaseModel
from models import User

# Crear un listado:
database = [{"id": 1, "name": "Juan Perez", "age": 25, "profesion": "Ingeniero"},
            {"id": 2, "name": "Susana Ruiz", "age": 45, "profesion": "Profesora"}]

# Creamos aplicación FastAPI:
app = FastAPI()

# Mostrar el listado: GET
@app.get("/mostrar/")
async def mostrar(response: Response):
    try:
        return database
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response.status_code
        
# Mostrar un registro con GET
@app.get("/mostrar/ {data_post} ")
async def mostrar(item_id: int, response: Response):

    # Accedemos al registro:
    for data_post in database:
        if data_post["id"]==item_id:

        # Mostramos el dato con ese ID los valores que nos lleguen:
            response.status_code = status.HTTP_200_OK
            return data_post

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"id":item_id , "msg":"User Not Found"}

# Insertar un dato en es listado: POST

@app.post("/insertar/", status_code=201)
async def insertarData(item: User, response: Response):
    # insertamos los valores
    data_post = ({"id": item.id,
                "name": item.name,
                "age": item.age,
                "profesion": item.profesion})

    database.append(data_post) 
    response.status_code = status.HTTP_201_CREATED
    # retornamos los valores que comprende el registro añadido
    return item


# Actualización de un dato del listado: PUT
@app.put("/ActualizarDato/{item_id}")
async def ActualizarDato(item_id: int, item:User,response: Response):

    # Accedemos al registro:
    for data_post in database:
        if data_post["id"]==item_id:
        # Modificamos el dato con ese ID los valores que nos lleguen:
            data_post["id"] = item.id
            data_post["name"] = item.name
            data_post["age"] = item.age
            data_post["profesion"] = item.profesion
            response.status_code = status.HTTP_200_OK
            return data_post
    response.status_code = status.HTTP_404_NOT_FOUND
    return data_post

# Eliminareis un dato: Delete

@app.delete("/BorrarDato/{item_id}")
async def BorrarDato(item_id: int,response: Response):
    # Accedemos al registro:
    for data_post in database:
        if data_post["id"]==item_id:
        # Eliminamos ese dato:
            database.remove(data_post)
            response.status_code = status.HTTP_204_NO_CONTENT
            return response.status_code
    response.status_code = status.HTTP_404_NOT_FOUND
    return response.status_code
    

# Eliminareis todos los datos: Delete

@app.delete("/BorrarBBDD/")
async def BorrarBBDD(response: Response):
    # Eliminamos ese dato:
    database.clear()
    response.status_code = status.HTTP_200_OK
    return response.status_code
