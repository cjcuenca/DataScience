from asyncio.windows_events import NULL
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="actividad", user="cjcuenca", password="DataScience2022",
                        host="localhost", port=5432)

cur = conn.cursor()

def createTablaEdiccion(cur):
    try:
        cur.execute("CREATE TABLE ediccion(ID_edic SERIAL PRIMARY KEY, name varchar(80));")    
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))

def createTablaNotas(cur):
    try:
        cur.execute("CREATE TABLE notas(ID_notas SERIAL PRIMARY KEY, name varchar(80), edad int, notas real, ID_ediccion int);")    
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))

#createTablaEdiccion(cur)
#createTablaNotas(cur)

def insertarEdiccion(cur):
    try:
        cur.execute("INSERT INTO ediccion (name) VALUES ('Uno')")
        cur.execute("INSERT INTO ediccion (name) VALUES ('Dos')")
        cur.execute("INSERT INTO ediccion (name) VALUES ('Tres')")
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))

#insertarEdiccion(cur)

def insertarNotas(cur):
    try:
        cur.execute("INSERT INTO notas (name, edad, notas, id_ediccion) VALUES ('Isabel Maniega',30, 5.6, 1)")
        cur.execute("INSERT INTO notas (name, edad, notas, id_ediccion) VALUES ('Jose Manuel Peña',30, 7.8, 1)")
        cur.execute("INSERT INTO notas (name, edad, notas, id_ediccion) VALUES ('Pedro López',25, 5.2, 2)")
        cur.execute("INSERT INTO notas (name, edad, notas, id_ediccion) VALUES ('Julia Garcia', 22, 7.3, 1)")
        cur.execute("INSERT INTO notas (name, edad, notas, id_ediccion) VALUES ('Amparo Mayora',28, 8.4, 3)")
        cur.execute("INSERT INTO notas (name, edad, notas, id_ediccion) VALUES ('Juan Martínez',30, 6.8, 3)")
        cur.execute("INSERT INTO notas (name, edad, notas, id_ediccion) VALUES ('Fernando López',35, 6.1, 2)")
        cur.execute("INSERT INTO notas (name, edad, notas, id_ediccion) VALUES ('María Castro',41, 5.9  , 3)")
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))

#insertarNotas(cur)

def actualizarNotas(cur):
    try:
        cur.execute("UPDATE notas SET notas=6.4 WHERE ID_notas=3;")
        cur.execute("UPDATE notas SET notas=5.2 WHERE ID_notas=8;")
    except psycopg2.Error as e:
        print("Error actualizar registro: %s" % str(e))

#actualizarNotas(cur)

def mostrar(cur):
    try:
        cur.execute("SELECT id_notas, notas.name, edad, notas, ediccion.name FROM notas INNER JOIN ediccion ON notas.id_ediccion = ediccion.id_edic;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

mostrar(cur)

def BuscarNotas(cur, nota_min, nota_max):
    try:
        cur.execute("SELECT id_notas, notas.name, edad, notas, ediccion.name FROM notas INNER JOIN ediccion ON notas.id_ediccion = ediccion.id_edic WHERE notas>="+str(nota_min)+"and notas<="+str(nota_max)+";")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

#BuscarNotas(cur, 5, 6.5)

def BuscarEdiccion(cur, numero):
    try:
        cur.execute("SELECT id_notas, notas.name, edad, notas, ediccion.name FROM notas INNER JOIN ediccion ON notas.id_ediccion = ediccion.id_edic WHERE ediccion.name='"+ str(numero) +"';")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

#BuscarEdiccion(cur, "Dos")

def delete(cur):
    try:
        cur.execute("DELETE FROM notas WHERE name='Pedro López'")
    except psycopg2.Error as e:
        print("Error actualizar registro: %s" % str(e))

#delete(cur)
#mostrar(cur)

conn.commit()

cur.close()
conn.close()