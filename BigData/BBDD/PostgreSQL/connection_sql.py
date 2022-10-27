# CRUD - Creat, Read, Update and Delete
# pip install psycopg2-binary

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(database="test", user="cjcuenca", password="DataScience2022",
                        host="localhost", port=5432)

cur = conn.cursor()

def createDatbase():
    conn = psycopg2.connect(user="cjcuenca", password="DataScience2022",
                            host="localhost", port=5432)

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()

    try:
        cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier("test")))
    except psycopg2.Error as e:
        print("Error al crear la base de datos: %s" % str(e))

    cur.close()
    conn.close()

# createDatbase()

def createTabla(cur):
    try:
        cur.execute("CREATE TABLE notas(name varchar(80), age int, grades real, date date);")
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))

# createTabla(cur)

def insertar(cur):
    try:
        cur.execute("INSERT INTO notas VALUES(%s, %s, %s, %s);", ('Jose Perez', 215, 8.6, '07/07/2022'))
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))

# insertar(cur)

def actualizar(cur):
    try:
        cur.execute("UPDATE notas SET grades=7.9 WHERE name='Jose Perez';")
    except psycopg2.Error as e:
        print("Error actualizar registro: %s" % str(e))

# actualizar(cur)

def delete(cur):
    try:
        cur.execute("DELETE FROM notas WHERE name='Jose Perez'")
    except psycopg2.Error as e:
        print("Error actualizar registro: %s" % str(e))

# delete(cur)

def mostrar(cur):
    try:
        cur.execute("SELECT * FROM notas;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

# mostrar(cur)

conn.commit()

cur.close()
conn.close()