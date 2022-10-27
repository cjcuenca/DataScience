from fastapi import FastAPI, status, Response
import pandas as pd 
import json
import csv
import os
from pydantic import BaseModel


# Creamos nuestra primera aplicación FastAPI:
app = FastAPI()

# doy la ruta donde se encuentra el dataset:
MEDIA_ROOT = "C:/Users/cjcue/Documents/GitHub/DataScience/media/iris.csv"

# Método GET a la url "/test/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get("/test/")
async def test_1():
    return "Bienvenido a FastAPI"


# Método GET para mostrar la información.
# Método GET a la url "/iris/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get("/iris/")
async def iris(response: Response):
    try:
        # Crear el dataframe con la información de iris:
        df = pd.read_csv(MEDIA_ROOT)
        # print(df)
        # lo transformamos a json para poder gestionarlo desde el front:
        data = df.to_json(orient="index")
        # cargar la información con formato Json:
        data = json.loads(data)
        return data
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "404 NOT FOUND"

# TODO: Realizar los distintos metodos con el IRIS dataset:
# Método POST para insertar un dato al final del iris dataset.

# Modelo de datos:
class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str 

# Método POST  a la url "/insertData/"
@app.post("/insertData/", status_code=201)
async def insertData(item: Iris):
    # leemos el archivo iris.csv e
    # insertar en la última línea los campos a insertar
    with open(MEDIA_ROOT, "a", newline="") as csvfile:
        # Nombres de los campos:
        fieldnames = ['sepal_length', 'sepal_width',
                      'petal_length', 'petal_width', 'species']
        # escribimos el csv:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # insertamos los valores en la última fila:
        writer.writerow({"sepal_length": item.sepal_length,
                         "sepal_width": item.sepal_width,
                         "petal_length": item.petal_length,
                         "petal_width": item.petal_width,
                         "species": item.species})
    # retornamos los valores que comprende la ultima fila añadida
    return item

# Método PUT a la url "/updateData/"
# llamaremos a nuestra aplicación (app.put)
@app.put("/updateData/{item_id}")
async def updateData(item_id: int, item:Iris):
    # Leemos el csv con ayuda de pandas:
    df = pd.read_csv(MEDIA_ROOT)
  
    # Modificamos el último dato con los valores que nos lleguen:
    # df.loc[df.index[-1], "sepal_length"] = item.sepal_length
    # df.loc[df.index[-1], "sepal_width"] = item.sepal_width
    # df.loc[df.index[-1], "petal_length"] = item.petal_length
    # df.loc[df.index[-1], "petal_width"] = item.petal_width
    # df.loc[df.index[-1], "species"] = item.species
   
    # Modificamos el dato con ese ID los valores que nos lleguen:
    # df.loc[df.index[item_id-2], "sepal_length"] = item.sepal_length
    # df.loc[df.index[item_id-2], "sepal_width"] = item.sepal_width
    # df.loc[df.index[item_id-2], "petal_length"] = item.petal_length
    # df.loc[df.index[item_id-2], "petal_width"] = item.petal_width
    # df.loc[df.index[item_id-2], "species"] = item.species

    # Modificamos el dato con ese ID los valores que nos lleguen:
    df.loc[item_id, "sepal_length"] = item.sepal_length
    df.loc[item_id, "sepal_width"] = item.sepal_width
    df.loc[item_id, "petal_length"] = item.petal_length
    df.loc[item_id, "petal_width"] = item.petal_width
    df.loc[item_id, "species"] = item.species

    # convertir a csv
    df.to_csv(MEDIA_ROOT, index=False)
    # Retornamos el id que hemos modificado y el dato en formato diccionario:
    return {"item_id": item_id, **item.dict()}

# Método DELETE para eliminar ese último dato del archivo.
# Método DELETE a la url "/deleteData/"
@app.delete("/deleteData/{item_id}")
async def deleteData(item_id: int):
    # Leemos el csv con ayuda de pandas:
    df = pd.read_csv(MEDIA_ROOT)
    # Eliminar la última fila:
    df.drop(df.index[-1], inplace=True)
    # convertir a csv
    df.to_csv(MEDIA_ROOT, index=False)
    return {"item_id": item_id, "msg": "Eliminado"}