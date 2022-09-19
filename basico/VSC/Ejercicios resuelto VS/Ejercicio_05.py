import numpy as np


# EJERCICIO 1

# a) Declara la variable "test" como una lista con los siguientes componentes: 25, 8, 32, 20, 1.
    # Usa las formas que conozcas para crearla y el uso de type para asegurarte de que es una lista.


def opcion_1():
    test = list((25, 8, 32, 20, 1))
    return test

# Descomentar para ejecutar:
# print(opcion_1())

def opcion_2():
    test = [25, 8, 32, 20, 1]
    return test

# Descomentar para ejecutar:
# print(opcion_2())

# b) Apendiza un valor de valor 20, 32, 25, 32

# una opción ...

def apendizar(x, lista):
    lista.append(x)
    return lista

test = apendizar(20, opcion_2())
test = apendizar(32, test)
test = apendizar(25, test)
test = apendizar(32, test)

# Descomentar para ejecutar:
# print(test)

# otra opción ...

def apendizar_2(listas, test_2):
    for value in listas:
        test_2.append(value)
    return test_2

listas = [20, 32, 25, 32]

# Descomentar para ejecutar:
# print(apendizar_2(listas, opcion_2()))


# c) Elimina el valor 8 de la lista

# print(test)



def eliminar(test):
    # Una opcion..
    # Eliminación por posición:
    # test.remove(test[1])

    # Otra opcion..
    # Eliminación por valor:
    test.remove(8)
    return test

# Descomentar para ejecutar:
# print(eliminar(test))


# d) Elimina los duplicados que haya en la lista test

def duplicados(test):
    return list(set(test))

# Descomentar para ejecutar:
test = duplicados(test)
# print(duplicados(test))

# e) Crea una segunda lista de nombre "info" que contenga los valores:
    #  25, 100, 10, 20, 5, 25, 30, 200

info = [25, 100, 10, 20, 5, 25, 30, 200]

# print(info)


# f) ¿Cuántos valores se repiten entre las listas?

# print("test: ", test)
# print("info: ", info)

def comparar(test, info):
    contador = 0
    for n in test:
        for i in info: # resultado: 20, 25, 25; total 3
            if n == i:
        # if n in info: # resultado: 20, 25; total 2
                print('Numero repetido: ', n)
                contador += 1
    return contador

# Descomentar para ejecutar:
# print(comparar(test, info))

# g) Muéstrame el maximo y mínimo en las dos listas

# Descomentar para ejecutar:
# print("## Máximo y mínimo de test: ")
# print(max(test))
# print(min(test))

# print("*** Máximo y mínimo de info")
# print(max(info))
# print(min(info))

def limites(test):
    return max(test), min(test)

# Descomentar para ejecutar:
# print(f" TEST - máximo: {limites(test)[0]}, mínimo: {limites(test)[1]}")

# print(f" INFO - máximo: {limites(info)[0]}, mínimo: {limites(info)[1]}")


# h) Crea una nueva variable de nombre "matriz" transformando la lista test en matriz

def matriz(lista_2):
    return np.array(lista_2)

# Descomentar para ejecutar:
# print(matriz(test))
# print(type(matriz(test)))


# i) Crea una función que se llame "funcion_división" donde se divida
    # el test con valor 32 entre info con valor 5 y muestra el resto de la división

def funcion_división(n, s):
    return test[n] % info[s]

def posicion(valor, listado):
    n = 0
    for i in listado:
        if i == valor:
            break
        n += 1
    return n

# print(posicion(32, test))
# print(posicion(5, info))

# Descomentar para ejecutar:
# print(funcion_división(posicion(32, test), posicion(5, info)))

# j) Con ayuda de reverse() muestra la inversa de test

# print(test)

def reverso(test_3):
    test_3.reverse()
    return test_3

# Descomentar para ejecutar:
# print(reverso(test))


# k) Con el listado info utiliza un bucle for con la ayuda de enumerate(),
    # para mostrar posición y valor y crea un diccionario de nombre "newDict"

def crear_diccionario(info):
    newDict = {}

    for key, value in enumerate(info):
        newDict[key] = value
    return newDict


# Descomentar para ejecutar:
# print(crear_diccionario(info))

# l) Crea un nuevo listado con nombre "info2" donde los valores: 25 se sustituya por "María",
    # el valor 20 por "Juan" y el valor 10 por "Pedro"

def transformar(listado):
    info2 = []

    for i in info:
        if i == 25:
            info2.append("María")
        elif i == 20:
            info2.append("Juan")
        elif i == 10:
            info2.append("Pedro")
        else:
            info2.append(i)
    return info2

# Descomentar para ejecutar:
# print(transformar(info))

# m) Sustituye en el listado test los multiplos de 2 por "Dos"

def multiplos(listado):
    n = 0
    for i in listado:
        if i%2 == 0:
            listado[n] = "Dos"
        n += 1
    return listado

# Descomentar para ejecutar:
# print(multiplos(test))


# EJERCICIO 2

"""
    Escribe un programa que imprima los números desde 1 hasta 100

    Pero:

    * Para los múltiplos de 3 escribe "Hello"
    * Para los múltiplos de 5 escribe "World"
    * Para los múltiplos de ambos (3 y 5) escribe "Hello World"
    (en vez de los números correspondientes)
"""

N = np.arange(0, 101, 1)
N = N.tolist()
print(np.array(N))

def sustituir(listado):
    for i in listado:
        if listado[i]%5 == 0:
            listado[i] = "Hello World"
        if listado[i]!="Hello World" and listado[i]%3 == 0:
            listado[i] = "Hello"
        if listado[i]!="Hello World" and listado[i]!="Hello" and listado[i]%5 == 0:
            listado[i] = "World"
    del listado[0]
    return np.array(listado)

# Descomentar para ejecutar:
print(sustituir(N))