import psycopg2 
from psycopg2 import sql 
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(database="actividad", user="IsaMan", password="cursoPython",
                        host="localhost", port=5432)

cur = conn.cursor()

ediciones = ["UNO", "DOS", "TRES"]

notas = [{"name": 'Isabel Maniega', "age": 30, "notas": 5.6, "id_ed": 1},
         {"name": 'José Manuel Peña', "age": 30, "notas": 7.8, "id_ed": 1},
         {"name": 'Pedro López', "age": 25, "notas": 8.4, "id_ed": 2},
         {"name": 'Amparo Mayora', "age": 28, "notas": 7.3, "id_ed": 3},
         {"name": 'Juan Martínez', "age": 30, "notas": 6.8, "id_ed": 3},
         {"name": 'Fernando López', "age": 35, "notas": 6.1, "id_ed": 2},
         {"name": 'María Castro', "age": 41, "notas": 5.9, "id_ed": 3},
         ]

def createDatabase():
    conn = psycopg2.connect(user="IsaMan", password="cursoPython",
                            host="localhost", port=5432)

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()

    try:
        cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier("test")))
    except psycopg2.Error as e:
        print("Error al crear la base de datos: %s" % str(e))

    cur.close()
    conn.close()

def createTablaNotas(cur):
    try:
        cur.execute("CREATE TABLE notas(ID_notas SERIAL PRIMARY KEY, name varchar(80), age int, grades real, ID_edic INT REFERENCES edicion(ID_edic));")
    except psycopg2.Error as e:
        print("Error crear la tabla Notas: %s" % str(e))

def createTablaEdicion(cur):
    try:
        cur.execute("CREATE TABLE edicion(ID_edic SERIAL PRIMARY KEY, Numero varchar(80));")
    except psycopg2.Error as e:
        print("Error crear la tabla Edicion: %s" % str(e))

# createTablaEdicion(cur)
# createTablaNotas(cur)

def insertarEdicion(cur, value):
    try:
        cur.execute(f"INSERT INTO edicion (Numero) VALUES('{value}');")
    except psycopg2.Error as e:
        print('Error Insertar dato: %s', str(e))

def insertarEdic(cur, ediciones):
    for edicion in ediciones:
        insertarEdicion(cur,edicion)

# insertarEdic(cur, ediciones)


def insertarNotas(cur, name:str, age:int, notas:float, ID_edic:int):
    try:
        cur.execute(f"INSERT INTO notas (Name, age, grades, ID_edic) VALUES('{name}', {age}, {notas}, {ID_edic});")
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))

def insertNotas(cur, notas):
    for nota in notas:
        insertarNotas(cur, nota['name'], nota['age'], nota['notas'], nota['id_ed'])

# insertNotas(cur, notas)


def actualizar(cur, tabla:str, nota:float, name:str):
    try:
        cur.execute(f"UPDATE {tabla} SET grades={nota} WHERE name='{name}';")
    except psycopg2.Error as e:
        print("Error actualizar registro: %s" % str(e))

# actualizar(cur, 'notas', 6.4, 'Pedro López')
# actualizar(cur, 'notas', 5.2, 'María Castro')

def mostrar(cur, tabla:str):
    try:
        cur.execute(f"SELECT * FROM {tabla};")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error mostrar registros: %s" % str(e))

# mostrar(cur, "notas")
# mostrar(cur, "edicion")

def filtrar(cur, tabla:str,column:str, nota1:float, nota2:float):
    cur.execute(f"SELECT * FROM {tabla} WHERE {column} BETWEEN {nota1} AND {nota2};") 
    rows = cur.fetchall()
    print(f"\n---- Datos en tabla {tabla} con {column} entre {nota1} y {nota2}--\n") 
    for row in rows:
        print(row)

# filtrar(cur, "notas", "grades", 5.0, 6.5)

def unirTablas(cur, tabla:str, value:str):
    cur.execute(f"SELECT * FROM {tabla} n INNER JOIN edicion e ON n.ID_edic = e.ID_edic WHERE numero = '{value}';")
    rows = cur.fetchall()
    print("\n---- Datos en de personas en la edicion DOS---\n")
    for row in rows:
        print(row)

# unirTablas(cur, "notas", 'DOS')

def delete(cur, tabla:str, name:str):
    try:
        cur.execute(f"DELETE FROM {tabla} WHERE name='{name}';")
    except psycopg2.Error as e:
        print('Error eliminar dato: %s', str(e))

delete(cur, 'notas', "Pedro López")

# Close communication with the database
conn.commit()
cur.close()
conn.close()