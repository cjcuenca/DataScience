import numpy as np


# EJERCICIO 1

"""
    Dada una lista de nombre "listado" y con valores: 10,20,30,40,50
"""
# 1) Crea un pequeño programa capaz de conseguir el orden inverso de los números de "listado"
# imprime nuevamente el listado para tenerlo "a mano"
# 10-20-30-40-50 (tengo)
# 50-40-30-20-10 (lo que busco)

listado = [10,20,30,40,50]

rango_indices = np.arange(1, len(listado)+1, 1).tolist()
# print(rango_indices)

def inverso(rango_indices, listado):
    listado_inverso = []                              # []
    for indice in rango_indices:                      # 1-2-3-4-5
        listado_inverso.append(listado[-indice])      # [1º]=> [50]--[50,40]--[50,40,30]--[50,40,30,20]--[50,40,30,20,10]

    return listado_inverso

# Descomentar para ejecutar:
# print(inverso(rango_indices, listado))


# EJERCICIO 2

"""
    Programa que coge por teclado 5 números y los almacena en una lista

    Nota:

    debería estar en la misma celda

    Hazlo como puedas, discurre cómo sería..
"""

def listado_teclado():
    listado_input = []

    for i in np.arange(1, 6):
        entrada = int(input("Escribe un número entero: "))
        listado_input.append(entrada)
    return listado_input

# Descomentar para ejecutar:
# print(listado_teclado())

# EJERCICIO 3

"""
    Programa que coge por teclado una frase y es capaz de decir cuántas vocales hay

    Nota: asume que son letras minúsculas sin tildes.
"""

# 1) Entrada de texto por teclado

# Descomentar para ejecutar:
# frase = input("añada una frase: ")
# print(frase)

# 2) Hazlo si puedes de varias formas
    # forma 1: contar vocales en palabra/frase

contador_vocales = 0 # contador a 0

vocales = ["a", "e", "i", "o", "u"]

def test_vocales(frase, contador_vocales):
    for letra in frase:
        if letra in vocales:
            contador_vocales+=1

    return contador_vocales

# Descomentar para ejecutar:
# print(test_vocales(frase, contador_vocales))

# 3) Hazlo de otra forma si se te ocurre..
    # forma 2

def test_vocales_2(frase, contador_vocales):
    for letra in frase:
        if (letra=="a") | (letra=="e") | (letra=="i") | (letra=="o") | (letra=="u"):
            contador_vocales += 1
    return contador_vocales

# Descomentar para ejecutar:
# print(test_vocales_2(frase, contador_vocales))


# EJERCICIO 4

"""
    Tablas de multiplicar:

    Haz algo tal que:
"""

# 1) Pregunta al usuario que tabla quiere multiplicar: <1 al 10>

tabla = int(input("Elija de que número quiere las Tablas de multiplicar: <1 a 10>: "))

# Descomentar para ejecutar:
# print(tabla)

# 2) Muestra los resultados de esta forma:

"""
    2 x 1 = 2

    2 x 2 = 4

    ...

    2 x 10 = 20
"""

numeros = np.arange(0, 11)
# print(numeros)

def tabla_multiplicar(numeros):
    for numero in numeros:
        print(tabla, " x ", numero, " = ", tabla*numero)

# Descomentar para ejecutar:
# tabla_multiplicar(numeros)

