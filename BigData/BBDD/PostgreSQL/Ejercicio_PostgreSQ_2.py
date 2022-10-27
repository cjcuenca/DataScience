from asyncio.windows_events import NULL
from mailbox import NoSuchMailboxError
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="actividad", user="cjcuenca", password="DataScience2022",
                        host="localhost", port=5432)

cur = conn.cursor()

def createTablaEdiccion(cur):
    try:
        query="CREATE TABLE ediccion"
        query = query + "(ID_edic SERIAL PRIMARY KEY, name varchar(80));" 
        cur.execute(query)   
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))

def createTablaNotas(cur):
    try:
        query="CREATE TABLE notas"
        query = query + "(ID_notas SERIAL PRIMARY KEY, name varchar(80)," 
        query = query + "edad int, notas real, ID_ediccion int);" 
        cur.execute(query)  
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))

#createTablaEdiccion(cur)
#createTablaNotas(cur)

nombres=("Uno", "Dos", "Tres")

def insertarEdiccion(cur, nombres):
    try:
        for i in range(len(nombres)):
            query="INSERT INTO ediccion (name) VALUES"
            query = query + "('" + nombres[i] + "')"
            cur.execute(query)  

    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))

#insertarEdiccion(cur, nombres)

db=list([
    ('Isabel Maniega',30, 5.6, 1),
    ('Jose Manuel Peña',30, 7.8, 1),
    ('Pedro López',25, 5.2, 2),
    ('Julia Garcia', 22, 7.3, 1),
    ('Amparo Mayora',28, 8.4, 3),
    ('Juan Martínez',30, 6.8, 3),
    ('Fernando López',35, 6.1, 2),
    ('María Castro',41, 5.9 , 3)
    ])
def insertarNotas(cur,db):
    try:
        for dato in db:
            query="INSERT INTO notas (name, edad, notas, id_ediccion) VALUES "
            query = query + str(dato)
            cur.execute(query)       
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))

#insertarNotas(cur,db)

def actualizarNotas(cur, id, valor):
    try:
        query="UPDATE notas SET notas="
        query = query + str(valor)
        query = query + " WHERE ID_notas=" + str(id) + ";"
        
        cur.execute(query)       
        print(query)

    except psycopg2.Error as e:
        print("Error actualizar registro: %s" % str(e))

#actualizarNotas(cur, 3, 6.4)
#actualizarNotas(cur, 8, 5.2)

def listar_tabla(cur, tabla):
    try:
        query="SELECT * FROM " + str(tabla + ";")        
        cur.execute(query)       
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

tabla="notas"
#listar_tabla(cur,tabla)

def mostrar(cur):
    try:
        query="SELECT id_notas, notas.name, edad, notas, ediccion.name "
        query = query + "FROM notas INNER JOIN ediccion "
        query = query + "ON notas.id_ediccion = ediccion.id_edic;"
        
        cur.execute(query)       

        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

#mostrar(cur)

def BuscarNotas(cur, nota_min, nota_max):
    try:
        query="SELECT id_notas, notas.name, edad, notas, ediccion.name "
        query = query + "FROM notas INNER JOIN ediccion "
        query = query + "ON notas.id_ediccion = ediccion.id_edic "
        query = query + "WHERE notas>="+str(nota_min)+" and notas<="+str(nota_max)+";"

        cur.execute(query)     

        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

#BuscarNotas(cur, 5, 6.5)

def BuscarEdiccion(cur, numero):
    try:
        query="SELECT id_notas, notas.name, edad, notas, ediccion.name FROM notas "
        query = query + "INNER JOIN ediccion ON notas.id_ediccion = ediccion.id_edic " 
        query = query + "WHERE ediccion.name='"+ str(numero) + "';" 
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

#BuscarEdiccion(cur, "Dos")

def delete(cur, nombre):
    try:
        query="DELETE FROM notas WHERE name='"
        query = query + nombre + "')" 
        cur.execute(query)
    except psycopg2.Error as e:
        print("Error actualizar registro: %s" % str(e))

#delete(cur, "Pedro López")
#mostrar(cur)

conn.commit()

cur.close()
conn.close()