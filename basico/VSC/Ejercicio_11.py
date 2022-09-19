"""
    Creado: Isabel Maniega
    Fecha: 08/09/2022
"""

# Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt


# EJERCICIO 1

"""
    Escribe el código necesario en Python para:

    almacenar con una lista de nombre "clientes" los siguientes nombres:

    "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas",
    "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"
"""

# 1) Para ese listado de clientes imprime todos ellos, 1 a 1

clientes = ["Ana Pérez", "Juan García", "Andres Álvarez",
            "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez",
            "Alberto Delgado", "Susana Castro", "Luis González"]

# Descomentar para ejecutar:
# print(clientes)

def imprimir(lista):
    try:
        for cliente in lista:
            print(cliente)
    except Exception as e:
        print("Error en bucle for %s" % str(e))

# Probar excepción:
# print(imprimir(1))

# Descomentar para ejecutar:
# imprimir(clientes)

"""
    2) Dentro de ese grupo de clientes..

    se pide buscar..al cliente de nombre: "Juan García" si es posible

    Si lo encuentra, debería imprimir un mensaje tal que así:

    "el cliente -nombre del cliente- se encuentra en mi Base de Datos de Clientes"

    Si no se le encuentra, debería salir un mensaje tal que así:

    "el cliente -nombre del cliente- NO se encuentra en mi Base de Datos de Clientes"

    Nota: Comprueba en el caso de llevar o no acento

    Para:

    Juan García

    Juan Garcia

    Ojo con la tilde..
"""



usuario = "Juan García"

usuario_2 = "Juan Garcia"

def buscar(clientes, usuario):
    for cliente in clientes:
        cliente_1 = cliente.lower()
        usuario_1 = usuario.lower()
        if cliente_1 == usuario_1:
            return f"El cliente {usuario} se encuentra en mi Base de Datos de Clientes"
    return f"el cliente {usuario} NO se encuentra en mi Base de Datos de Clientes"

# Descomentar para ejecutar:
# print(buscar(clientes, usuario))
# print(buscar(clientes, usuario_2))

# Otra opción..

def buscar_2(clientes, user):
    user_1 = user.lower()
    # Como pasar la lista a minúsculas (3 opciones):

    # opción 1)
    a = (map(lambda x: x.lower(), clientes))
    clientes = list(a)

     # opción 2)
    # a = [x.lower() for x in clientes]

     # opción 3)
    # pd_d = list(pd.Series(clientes).str.lower())
    # print(pd_d)

    if user_1 in clientes:
        return f"El cliente {user} se encuentra en mi Base de Datos de Clientes"
    else:
        return f"el cliente {user} NO se encuentra en mi Base de Datos de Clientes"

# Descomentar para ejecutar:
# print(buscar_2(clientes, usuario))
# print(buscar_2(clientes, usuario_2))

"""
    3) Crea un DataFrame, de nombre df

    con esa información en base a la siguiente relación de clientes y tarifas contratadas (€)

    clientes: Ana Pérez, Juan García, Andrés Álvarez, Luis Ramos, Pedro Cadenas,
            Estefanía Miguélez, Alberto Delgado, Susana Castro, Luis González

    tarifas: 40,50,50,35,45,50,60,50,45
"""

tarifas = [40, 50, 50,
           35, 45, 50,
           60, 50, 45]

df = pd.DataFrame({"Clientes": clientes, "Tarifas": tarifas})

# Descomentar para ejecutar:
# print(df)

# 4) Imprime las primeras 5 filas del DataFrame de 2 formas distintas

# Descomentar para ejecutar:
# print(df.head())

# Descomentar para ejecutar, ver las últimas filas:
# print(df.tail())

# 5) De ese DataFrame, selecciona solamente la columna "tarifas" e imprímela
    # (con 1 forma es suficiente, pero si sabes 2 mejor)

# Descomentar para ejecutar:
# print(df[["Tarifas"]])

# print(df.Tarifas)

# print(df['Tarifas'])

# 6) Descomenta las siguientes líneas (algunos trucos y cosas útiles).
    # Ponlo en formato función!!

def counts(df):
    return df.Tarifas.value_counts()

# Descomentar para ejecutar:
# print(counts(df))

def grafico(df):
    df.Tarifas.value_counts().plot(kind="bar")
    plt.show()

# Descomentar para ejecutar:
# grafico(df)

def grafico_main(df):
    df.Tarifas.plot(kind="bar")
    plt.show()

# Descomentar para ejecutar:
# grafico_main(df)

# Pasando sólo el nombre de la columna
def grafico_test(df, column):
    df[[column]].plot(kind="bar")
    plt.show()

column = "Tarifas"

# Descomentar para ejecutar:
# grafico_test(df, column)

# print(df)

# 7) De ese DataFrame, selecciona solamente aquellos clientes con tarifa superior a 50 euros (50 no incluído)

def superior_50(df):
    return df[df["Tarifas"] > 50]

# Descomentar para ejecutar:
# print(superior_50(df))


# EJERCICIO 2

# Número par o impar

# Prueba para los números 6 y 3

# Realiza un algortimo para saber si son pares o impares


def comprobar(numero):
    if numero % 2 == 0:
        return f"El numero {numero} es PAR"
    else:
        return f"El número {numero} es IMPAR"

# Descomentar para ejecutar:
# print(comprobar(6))
# print(comprobar(3))


# EJERCICIO 3

"""
    Intercambio de valores entre variables

    Siendo por ejemplo:

    x = 3 e y = 2
    Se pide hacer un pequeño algoritmo que me intercambie esos valores.

    Y que sea el resultado:

    x = 2 e y = 3
"""

# 1) Hazlo sin funciones

x, y = 3, 2

# Descomentar para ejecutar:
# print(x, y)

aux = x

x = y

y = aux

# Descomentar para ejecutar:
# print(x, y)


# 2) Hazlo mismo con una función

def intercambio(x, y):
    aux = x
    x = y
    y = aux
    return x, y

x, y = intercambio(3, 2)

# Descomentar para ejecutar:
# print(x, y)