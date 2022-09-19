import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# EJERCICIO 1

# NO HACE FALTA HACERLO EN FORMATO FUNCIÓN!

# Se pide por tanto:

# -1- Leer el archivo train.csv de Titanic dataset con pandas (carpeta src)

df = pd.read_csv("./src/train.csv")

# Descomentar para ejecutar:
# print(df)

# -2- Imprimir algunas filas de la parte de arriba y otras de la parte del final

# Descomentar para ejecutar:
# print(df.head(3))
# print(df.tail(3))

# -3- Imprimir algunos parámetros estadísticos

# Descomentar para ejecutar:
# print(df.describe())

# -4- Ver si en todas las columnas tenemos el mismo número de datos (solo verlo)

# Descomentar para ejecutar:
# print(df.shape, df.size)

# -5- Ver el número de hombres y mujeres que hay

# Descomentar para ejecutar:
# print(df.Sex.value_counts())

# -6- Hacer alguna gráfica con pandas relativa al número de hombres y mujeres que hay

df.Sex.value_counts().plot(kind="bar")
# Descomentar para ejecutar:
# plt.show()

# Si quieres hacer alguna cosa más también puedes

df.Survived.value_counts().plot(kind="bar")
# Descomentar para ejecutar:
# plt.show()

# EJERCICIO 2
"""
    Dadas estas matrices:

    * m1 = [[1, 10, 20], [30, 40, 50]]
    * m2 = [[60, 80, 90,]]
    * m3 = [[-2, 3, 5], [8, 6, 2]]
"""

m1 = np.array([[1, 10, 20], [30, 40, 50]])
m2 = np.array([[60, 80, 90,]])
m3 = np.array([[-2, 3, 5], [8, 6, 2]])

# Descomentar para ejecutar:
# print(m1)
# print(m2)
# print(m3)

# 1) Comprueba si todos los valores de las matrices son mayores de 0

def mayores_0(matriz):
    return np.all(matriz > 0)

# Si son mayores == True; si no False
# Descomentar para ejecutar:
# print(mayores_0(m1)) # True
# print(mayores_0(m2)) # True
# print(mayores_0(m3)) # False

# 2) Si en la matriz m2 se encuentra el valor 80

def encontrar(matriz, valor):
    return valor in matriz

# Si está == True; si no False
# Descomentar para ejecutar:
# print(encontrar(m2, 80)) # True

# 3) Selecciona de m1 las dos últimas columnas

# Descomentar para ejecutar:
# print(m1[:, [1, 2]])

# 4) Concatena la m1 con m2, cuyo nombre de la matriz resultante sea m4

m4 = np.concatenate((m1, m2), axis=0)

# Descomentar para ejecutar:
# print(m4)

# 5) Convierte m1 y m3 en "np.matrix" asignando el nombre de matriz_1 y matriz_3, respectivamente

matriz_1 = np.matrix(m1)

# Descomentar para ejecutar:
# print(matriz_1)

# print("matriz inicial (m1): ", type(m1))
# print("matriz final (matriz_1): ", type(matriz_1))

matriz_3 = np.matrix(m3)

# Descomentar para ejecutar:
# print(matriz_3)

# 6) Realiza la resta, suma y producto de la matriz_1 y matriz_3

# Suma:

def suma_matrices(matriz_1, matriz_3):
    return matriz_1 + matriz_3

# Descomentar para ejecutar:
# print(suma_matrices(matriz_1, matriz_3))

# Resta:

def resta_matrices(matriz_1, matriz_3):
    return matriz_1 - matriz_3

# Descomentar para ejecutar:
# print(resta_matrices(matriz_1, matriz_3))

# Producto:

def producto_matrices(matriz_1, matriz_3):
    return matriz_1 * matriz_3.T

# Descomentar para ejecutar:
# print(producto_matrices(matriz_1, matriz_3))



# 7) Realiza las traza de la matriz de m4

# Descomentar para ejecutar:
# print(np.trace(m4))



# EJERCICIO 3

"""
    * Numeros Primos: Crear un listado de los numeros primos menores de 30

    Explicación inicial teórica

    (véase Tema_7..)

    Nota:

    si quieres apendiza el número 2,

    y a partir de ahí crea el algoritmo para apendizar los demas

    (menores de 30 en todo caso)

"""

# 1) Pide por teclado un número y di si es o no primo

# numero = int(input("Elija un número entero y le diré si es primo o no: "))

# Descomentar para ejecutar:
# print(numero)

def primos(numero):
    listado_restos = []
    for n in range(2, numero, 1):
        listado_restos.append(numero % n)

    if 0 not in listado_restos:
        return f"El número {numero} es primo"
    else:
        return f"El número {numero} No es primo"

# Descomentar para ejecutar:
# print(primos(numero))

# 2) Escribe los números primos menores de 30

def primos_2(inicio, fin):
    primos = []
    primos.append(2)

    for n in np.arange(inicio, fin, 1):
        listado_restos = []
        for i in np.arange(2, n):
            listado_restos.append(n % i)
        if 0 not in listado_restos:
            primos.append(n)
    return np.array(primos)

# Descomentar para ejecutar:
# print(primos_2(3, 30))

# 3) Numeros Primos: Crear un listado de los numeros primos menores de 200

# Descomentar para ejecutar:
# print(primos_2(3, 200))

# 4) Números Primos: Haz un listado de números primos entre 50 y 100

# Descomentar para ejecutar:
# TODO:  Pensar como eliminar el 2 de la lista!!!
# print(primos_2(50, 100))


# 5) Numeros Primos: Haz un listado de los 10 primeros números primos
    # Si puedes hazlo de más de una forma, no necesario aun así

def primos_3(inicio, fin):
    primos = []
    primos.append(2)

    for n in np.arange(inicio, fin, 1):
        listado_restos = []
        for i in np.arange(2, n):
            listado_restos.append(n % i)
        if 0 not in listado_restos and len(primos) < 10:
            primos.append(n)
    return np.array(primos)

# Descomentar para ejecutar:
# print(primos_3(3, 200))