import pandas as pd
import matplotlib.pyplot as plt

# EJERCICIO 1

# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo
listado = [30, 20, 10, 50, 40]

# Descomentar para ejecutar:
# print(listado)

# 2) Prueba con min(listado)

def minimo(lista):
    return min(lista)

# Descomentar para ejecutar:
# print(minimo(listado))

# 3) Realiza lo mismo pero con bucles y condicionales

# una opción...

def minimo_2(lista):
    minimo = max(lista) + 1

    for numero in lista:
        if numero < minimo:
            minimo = numero

    return minimo

# Descomentar para ejecutar:
# print(minimo_2(listado))

# otra opción...

def minimo_3(lista):
    minimo = 1000000

    for numero in listado:
        if numero < minimo:
            minimo = numero

    return minimo

# Descomentar para ejecutar:
# print(minimo_3(listado))


# EJERCICIO 2

# Máximo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

# Descomentar para ejecutar:
# print(listado)

# 2) Prueba con max(listado)

def maximo(lista):
    return max(lista)

# Descomentar para ejecutar:
# print(maximo(listado))

# 3) Realiza lo mismo pero con bucles y condicionales

# una opción...

def maximo_1(lista):
    maximo = -100000000

    for numero in listado:
        if numero > maximo:
            maximo = numero
    return maximo

# Descomentar para ejecutar:
# print(maximo_1(listado))

# otra opción...

def maximo_2(lista):
    maximo = -min(listado)-1

    for numero in listado:
        if numero > maximo:
            maximo = numero
    return maximo


# print(maximo_2(listado))


# EJERCICIO 3

# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"

# 1) Escribe el listado e ímprimelo

# Descomentar para ejecutar:
# print(listado)

# 2) Prueba a usar sort()

def colocar(lista):
    lista.sort(reverse=False)
    return lista

# Descomentar para ejecutar:
# print(colocar(listado))

# 3) Realiza lo mismo pero con bucles y condicionales

# me creo una copia para no perder la información
listado_copia = listado.copy()

# Descomentar para ejecutar:
# print(listado_copia)

def colocar_2(lista):
    listado_ascendente=[]                            # listado vacío

    while(len(lista) > 0):                           # mientras que tenemos números en listado->longitud(listado) distinta de 0
        listado_ascendente.append(min(lista))      # apendizas el mínimo
        lista.remove(min(lista))                 # le borras del listado original

    return listado_ascendente

# Descomentar para ejecutar:
# print(colocar_2(listado_copia))



# EJERCICIO 4

# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# 1) Escribe el listado e ímprimelo

# Descomentar para ejecutar:
# print(listado)

# 2) Prueba a usar sort()

def colocar_3(lista):
    lista.sort(reverse=True)
    return lista

# Descomentar para ejecutar:
# print(colocar_3(listado))

# 3) Realiza lo mismo pero con bucles y condicionales

# Descomentar para ejecutar:
# print(listado_copia)

def colocar_4(lista):
    listado_ascendente=[]                            # listado vacío

    while(len(lista) > 0):                           # mientras que tenemos números en listado->longitud(listado) distinta de 0
        listado_ascendente.append(max(lista))      # apendizas el mínimo
        lista.remove(max(lista))                 # le borras del listado original

    return listado_ascendente

# Descomentar para ejecutar:
# print(colocar_4(listado_copia))


# EJERCICIO 5
"""
    Escribe el código necesario en Python para:

    * almacenar con una lista de nombre "módulos" las siguientes materias de un programa de Ciencia de Datos:

    * Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP.

"""
# 1) Para ese listado imprime todas ellas, 1 a 1

modulos = ['Big Data', 'Python', 'Algoritmos', 'Machine Learning', 'Deep Learning', 'NLP']
# print(modulos)

def iteracion(lista):
    for i in lista:
        print(i)

# Descomentar para ejecutar:
# iteracion(modulos)

"""
    2) dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas.

    y que forman la base de conocimientos iniciales para afrontar con éxito el resto de un programa.

    Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas)

    Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales" (por ejemplo)

    Imprime ese listado al terminar de almacenarlos.
"""

def materias_esenciales(lista):
    esenciales = []
    for modulo in lista:
        if modulo == "Python" or modulo == "Algoritmos":
            esenciales.append(modulo)
    return esenciales

# Descomentar para ejecutar:
# print(materias_esenciales(modulos))

"""
    3) Crea un DataFrame, de nombre df con esa información en base
    a la siguiente relación de módulos y horas de clase módulos:
    Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP

    horas: 25, 15, 5, 15, 5, 10
"""

horas = [25, 15, 5, 15, 5, 10]

df = pd.DataFrame({"Modulos": modulos, "Horas": horas})

# Descomentar para ejecutar:
# print(df)

# 4) De ese DataFrame, selecciona solamente la columna "horas" e imprímela

# Descomentar para ejecutar:
# print(df["Horas"]) # Primera opción

# print(df.Horas) # Segunda opción

# print(df[["Horas"]]) # Tercera opción

# 5) Muestra el gráfico (plot) para la columna "horas"

figure = df.Horas.plot(kind="bar")

# Descomentar para ejecutar:
# plt.show()

# 6) De ese DataFrame, selecciona solamente aquellas materias que tienen 20 o más horas de dedicación

def mas_20(df):
    return df[df["Horas"] >= 20]

# Descomentar para ejecutar:
# print(mas_20(df))

# 7) De ese DataFrame, selecciona solamente aquellas materias que tienen menos de 10 horas de dedicación

def menos_10(df):
    return df[df["Horas"] < 10]

# Descomentar para ejecutar:
# print(menos_10(df))

# 8) De ese DataFrame, selecciona solamente (si fuera posible)
    # aquellas materias que tienen mas de 26 horas de dedicación

def mas_26(df):
    return df[df["Horas"] > 26]

# Descomentar para ejecutar:
# print(mas_26(df))

# 9) Apendiza, (si puedes), una nueva columna llamada "docente" con el instructor encargado de la materia.

    # Y cuyos nombres serán: Enrique, Susana, Juan, Ana, Laura, Patricia

df["docente"] = ['Enrique', 'Susana', 'Juan', 'Ana', 'Laura', 'Patricia']

# Descomentar para ejecutar:
# print(df)

