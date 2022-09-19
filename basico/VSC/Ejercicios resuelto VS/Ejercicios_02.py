import pandas as pd

# EJERCICIO 1

"""
   Dado el siguiente listado: ["Python", "Matlab", "R", "VBA", "Julia", "C++"].

    Modifica con un algoritmo ese listado.

    Cuando encuentre Python debe poner un 1
    y cuando encuentre otro lenguaje de programacion, un 0
    es un simple ejemplo de modificación de valores en una lista.
"""

languages =  ["Python", "Matlab", "R", "VBA", "Julia", "C++"]
# print(languages)

def transformacion(languages):
    for i in range(len(languages)):
        if languages[i] == "Python":
            languages[i] = 1
        else:
            languages[i] = 0
    return languages

# Descomentar para ejecutar:
# print(transformacion(languages))

# EJERCICIO 2

"""
    Dada la siguiente lista:
    L = [10, None, 8, 5, None, 20]
"""
L = [10, None, 8, 5, None, 20]

# 1) Susitituir por -1 el valor None usando bucles y listas

def sustitución(L):
    for i in range(0, len(L)):
        if L[i] == None:
            L[i] = -1
    return L

# Descomentar para ejecutar:
# print(sustitución(L))

# 2) Creamos un dataframe con los valores de la lista y
#     modificamos los "NaN" por un valor de -1 (Valores nulos, suma, etc..)
df = pd.DataFrame(L, columns=["listado"])

# Descomentar para ejecutar:
# print(df)

# Descomentar para ejecutar:
# print("Dataframe valores nulos", df.isnull())
# print("Suma valores nulos",df.isnull().sum())

def sustitución_2(df):
    df.listado = df.listado.fillna(-1)
    return df

# Descomentar para ejecutar:
# print(sustitución_2(df))


# 3) Vuelve a escribir el listado con falta de valores (inicial),
#     y sustituye por la media.

def sustitución_3(df):
    df.listado = df.listado.fillna(df.listado.mean())
    return df

# Descomentar para ejecutar:
# print(sustitución_3(df))


# 4) Apendiza la columna con estos valores
#     listado2 = [10, 20, 50, 30, 20, 0]

listado2 = [10, 20, 50, 30, 20, 0]

def appendColumn(df, listado2):
    df['listado2'] = listado2
    return df

# Descomentar para ejecutar:
# print(appendColumn(df, listado2))

df_2 = appendColumn(df, listado2)

# 5) Elimina la columna L

def deleteColumn(df_2):
    df_2 = df_2.drop(["listado2"], axis=1)
    return df_2

# Descomentar para ejecutar:
# print(deleteColumn(df_2))
# print(df)

# EJERCICIO 3

"""
    Crear un listado con los siguientes numeros:
        10, 20, 30, 40 (nombra la lista con nombre: "listado")
"""
listado = [10, 20, 30, 40]

# 1) Crea el listado e imprimelo:

# Descomentar para ejecutar:
# print(listado)

# 2) Apendiza el valor 50 ( si es posible)

def appendValue(listado, numero):
    listado.append(numero)
    return listado

# Descomentar para ejecutar:
# print(appendValue(listado, 50))

# listado_3 = appendValue(listado, 50)



# 3) Modifica (si es posible) el valor 10 por 100

def modificacion(listado, numero):
    listado[0] = numero
    return listado

# Descomentar para ejecutar:
# print(modificacion(listado_3, 100))

# EJERCICIO 4

"""
    Dada una lista de nombre "Temperatura" con valores: 10, 20, 30, 40, 50
"""
Temperatura = [10, 20, 30, 40, 50]

# 1) Crea el listado e imprimelo:

# Descomentar para ejecutar:
# print(Temperatura)

# 2) En este "Temperatura". ¿Cuál es el elemento en la posición (index) 1?

def indexValue(lista, indexado):
    return lista[indexado]

# Descomentar para ejecutar:
# print(indexValue(Temperatura, 1))

# 3) ¿Y en la posición (index) 0?

# Descomentar para ejecutar:
# print(indexValue(Temperatura, 0))

# 4) ¿Y en la posición (index) -1?

# Descomentar para ejecutar:
# print(indexValue(Temperatura, -1))

# print(indexValue(listado, -1))

