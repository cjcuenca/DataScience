import pymongo
import pandas as pd
import yfinance as yf

class crud:
    # FUNCIONES
    def insertDocument(nombredb, coleccion, db):
        # IMPORTAMOS LOS DATOS DE Y FINANCE
        # Vamos a extraer las cotizaciones de Google en las mencionadas
        # Año 2015-2016-2017-2018
        # formato: Año-Mes-Día
        df_y = yf.download("GOOGL", "2015-1-1", "2018-12-31")
        
        # Lo convertimos en lista de diccionarios
        df_y_dic = df_y.to_dict('records')

        # conexión a base de datos
        bbdd = pymongo.MongoClient("localhost", 27017)

        # Si no existe la base de datos la crea con el nombre qye haya en nombredb
        db = bbdd[nombredb]

        # print(db.list_collection_names())
        insertDocument(db, coleccion, df_y_dic)
        db[coleccion].insert_many(df_y)

        #mostrar_datos_coleccion(db, coleccion)

    def mostrar_datos_coleccion(database, coleccion):
        datos = database[coleccion].find({})
        for dato in datos:
            print(dato)



# POST BBDD YFinance
@app.post("/insertYFinance/", status_code=status.HTTP_200_OK, tags=["TERMINADO"],
         description="Carga cotización Google de YFinance")
async def insertManyEx(response: Response):
    
    nombredb="DFGoogle"
    coleccion="Yfinance"
    insertDocument(nombredb, coleccion, db)
    response.status_code = status.HTTP_200_OK
    return "Tabla Creada y datos YFinance cargados"