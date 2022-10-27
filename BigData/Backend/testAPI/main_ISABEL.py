from fastapi import FastAPI, status, Response

from pydantic import BaseModel
from models import User

tags_metadata = [
    {"name":"TEST",
    "description":"Bienvenida",
    },
    {
    "name":"Users",
    "description":"Muestra los gestión de los usuarios",
    },
]


# Creamos aplicación FastAPI:
app = FastAPI (title = "DataScience Course",
                openapi_tags = tags_metadata,
                contact = {"name" : "Isabel Maniega",
                            "url" : "https://es.linkedin.com/in/isabel-maniega-cuadrado-4",
                            "email" : "isabelmaniega@hotmail.com",
                    },
                openapi_url="/api/v0.1/openapi.json")

# Crear un listado:
database = [{"id": 1, "name": "Juan Perez", "age": 25, "profesion": "Ingeniero"},
            {"id": 2, "name": "Susana Ruiz", "age": 45, "profesion": "Profesora"}]

# Declarar el primer método GET para información de la WEB y tenga en cuenta la etiqueta Test:
@app.get("/", tags = ["TEST"], description = "Mostrar la información de la WEB")
async def info():
    return {"msg":"Bienvenido a nuestra Api Rest"}


# Mostrar el listado: GET
@app.get("/getData/", status_code = status.HTTP_200_OK, tags = ["Users"], 
                    description = "Mostrar todos los usuarios")
async def show():
    return database
        
# Mostrar un registro con /getData/{id}
@app.get("/getData/{id}", status_code = status.HTTP_200_OK,
                                tags = ["Users"],
                                description ="Mostrar un usuario")
async def show(id: int, response: Response):

    for i in range(0, len(database)):
        if database[i]["id"]==id:
            response.status_code = status.HTTP_200_OK
            return database[i]

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"id":id , "msg":"User Not Found"}

# Insertar un dato en es listado: POST

@app.post("/postData/", status_code=status.HTTP_201_CREATED,
                        tags=["Users"], 
                        description="Insertar un usuario")
async def insert(item: User):
    # apendizar el diccionario en la lista
    database.append(item.dict())
    return item


# Actualización de un dato del listado: PUT
@app.put("/putData/{id}", status_code=status.HTTP_200_OK, tags=["Users"],
                            description="Actualizar un usuario")
async def update(id: int, item:User,response: Response):

    # Accedemos al registro:
    for i in range(0,len(database)):
        if database[i]["id"]==id:
        # Modificamos el dato con ese ID los valores que nos lleguen:
            database[i] = item.dict()
            response.status_code = status.HTTP_200_OK
            return item, {"id":id , "msg":"Modificado"}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"id":id , "msg":"User Not Found"}

# Eliminareis un dato: Delete

@app.delete("/deleteData/{id}", tags=["Users"],
                            description="Eliminar un usuario")
async def delete(id: int,response: Response):

    for value in database:
        if value["id"]==id:
            database.remove(value)
            response.status_code = status.HTTP_204_NO_CONTENT
            return {"id":id , "msg":"Eliminado"} #no muestra nada al ser error 204
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"id":id , "msg":"User Not Found"}
    

# Eliminareis todos los datos: Delete

@app.delete("/deleteData/", tags=["Users"],
                            description="Eliminar todos los usuario")
async def delete(response: Response):
    database.clear()
    response.status_code = status.HTTP_200_OK
    return {"msg": []}
