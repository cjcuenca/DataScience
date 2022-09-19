import pandas as pd
import time
import numpy as np



# EJERCICIO 1

# Calcula la longitud de una cadena de texto sin usar la instruccion len(cadena)

# 1) Cadena de texto: hola como estas?

    # Nombre de la variable: "cadena"
cadena = "hola como estas?"

# Descomentar para ejecutar:
# print(cadena)

# 2) Longitud de la cadena de texto

# Descomentar para ejecutar:
# print(len(cadena))

# 3) Longitud de la cadena de texto calculada con un bucle

def longitud(cadena):
    contador = 0
    for letra in cadena:
        contador += 1
    return contador

# Descomentar para ejecutar:
# print(longitud(cadena))


# EJERCICIO 2

# Crea un diccionario que tenga la nota de 3 asignaturas y

# haz un pequeño algoritmo que calcule la nota media

# CURSO         -> Nota
# ---------------------
# Python        ->  10
# Big Data      ->  8
# NLP           ->  6

notas = {"Python": 10, "Big Data": 8, "NLP": 6}
# print(notas)

values = [value for value in notas.values()]
# Descomentar para ejecutar:
# print(values)

media = sum(values) / len(values)
# Descomentar para ejecutar:
# print(media)


# 1) Muestra el valor de las claves

def claves(diccionario):
    return diccionario.keys()

# Descomentar para ejecutar:
# print(claves(notas))

# 2) Muestra el valor de los valores del diccionario

def valores(diccionario):
    return diccionario.values()

# Descomentar para ejecutar:
# print(valores(notas))

# 3) Apendiza en el diccionario un nuevo elemento:

    # Machine Learning --> 9

notas["Machine Learning"] = 9

# Descomentar para ejecutar:
# print(notas)

# 4) Haciendo uso un bucle muestra la clave y el valor del diccionario, cuyo resultado final sean listas anidadas.

    # [["clave1", valor1], ["clave2", valor2]]

def anidada(diccionario):
    list_main = []
    for key, value in diccionario.items():
        list_info = []
        list_info.append(key)
        list_info.append(value)
        # print(list_info)
        list_main.append(list_info)
    return list_main

# Descomentar para ejecutar:
# print(anidada(notas))


# 5) Reconvierte el diccionario para transformarlo en un dataframe y busca la asignatura con la nota más alta

curso = ["Python", "Big Data", "NLP", "Machine Learning"]
grades = [10, 8, 6, 9]

data = {"Asignatura": curso, "Notas": grades}

df = pd.DataFrame(data)

# Descomentar para ejecutar:
# print(df)

mayor = max(df.Notas)

# Descomentar para ejecutar:
# print("Nota más alta: ", mayor)

# 6) ¿y la nota más baja?


baja = min(df.Notas)

# Descomentar para ejecutar:
# print("Nota más baja: ", baja)

# 7) Ordena el dataframe en orden descendente:

# Descomentar para ejecutar:
# print(df.sort_values(by="Notas", ascending=False))

# EJERCICIO 3

"""
Dadas 2 funciones:

Determina cual de ellas ejecuta mas rápido.

Si sabes, hazlo de 2 formas.

función a

def main(): for i in range(10**8): pass

main()

función b

def main(): for i in np.arange(10**8): pass

main()
"""

inicial = time.time()

def main():
    for i in range(10**8):
        pass

# Descomentar para ejecutar:
# main()

final = time.time()

# Descomentar para ejecutar:
# print(f"Tiempo de ejecucion (range): {final - inicial}")


inicial_1 = time.time()

def main_2():
    for i in np.arange(10**8):
        pass

# Descomentar para ejecutar:
# main_2()

final_1 = time.time()

# Descomentar para ejecutar:
# print(f"Tiempo de ejecucion (np.arange): {final_1 - inicial_1}")


# EJERCICIO 4

# Dada:

# Una matriz tal que así:

# A = np.array([[1,2,3], [4,5,6], [7,8,9]])

# se pide:

# 1) Escribe ese código en Python

A = np.array([[1,2,3], [4,5,6], [7,8,9]])

# Descomentar para ejecutar:
# print(A)

# 2) Escribe la matriz transpuesta.

    # Nota, puedes usar numpy, si quieres. Si sabes más de una forma puedes usar varias.

# print(A.T)

# 3) Se pide que hagas lo mismo, pero con un bucle.

def transpuesta():
    list_main = []
    for i in range(3):
        list_row = []
        for j in range(3):
            list_row.append(A[j][i])
        list_main.append(list_row)
    trans = np.array(list_main)
    return trans

# Descomentar para ejecutar:
# print(transpuesta())