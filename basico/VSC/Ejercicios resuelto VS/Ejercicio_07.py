import numpy as np
from time import sleep


# EJERCICIO 1

"""
    Dado: "np.arange(2,10)"

    sigue los siguientes pasos:

    1) Escribe esa instrucción y asígnaselo a la variable "a"
"""

a = np.arange(2,10)

# Descomentar para ejecutar:
# print("A: ", a)
# print("A tipo: ", type(a))

# 2) ¿Es equivalente a "np.arange(2,10,1)"?

b = np.arange(2,10,1)

# Descomentar para ejecutar:
# print("B: ", b)

# Sí, son equivalentes

# 3) Se pide quedarse con aquellos números menores de 5.

    # hazlo con numpy si puedes para la variable "a"


def menores_5(a):
    menor_5 = []

    for numero in a:
        if numero < 5:
            menor_5.append(numero)
    return menor_5

# Descomentar para ejecutar:
# print(menores_5(a))

# 4) Hazlo pasando esa información (de "a") a una lista

def convert_list(a):
    return a.tolist()

# Descomentar para ejecutar:
# print(convert_list(a))
# print("A tipo: ", type(convert_list(a)))

# 5) En base a los resultados..

    # ¿Es posible recorrer 1 a 1 un array de numpy?

# Sí, es posible

# 6) Haz el mismo proceso programando una sola línea (toma "a" como referencia)

def unaLinea(a):
    return [numero for numero in a if numero < 5]

# Descomentar para ejecutar:
# print(unaLinea(a))

# EJERCICIO 2

"""
    Para estos valores (v de valores por abreviar):

    v1 = 4

    v2 = 5

    v3 = 7

    v4 = 8

    El objetivo será calcular la media de estos valores

    Para ello sigue los siguientes pasos:

"""

# 1) Imprime los valores de esas variables v1,v2,v3,v4

v1 = 4

v2 = 5

v3 = 7

v4 = 8

# Descomentar para ejecutar:
# print(v1, v2, v3, v4)


# 2) Descomenta las 2 líneas siguientes para aprender..

    # que es posible asignar varios valores en la misma línea

    # Y la asignación de valores a variables se hace de forma consecutiva.

# v1,v2,v3,v4 = 4, 5, 7, 8
# print(v1,v2,v3,v4)

#3) Descomenta la línea siguiente para aprender una posible forma de calcular la media.

    #  Usamos nuevamente numpy..

# media_numpy = np.mean([v1,v2,v3,v4])

# print(media_numpy)


# 4) Calcula la media sin usar numpy

    # Si el resultado no sale bien, razona cómo debería hacerse..

def media(v1,v2,v3,v4):
    return (v1 + v2 + v3 + v4) /4

# Descomentar para ejecutar:
# print(media(4,5,7,8))


# EJERCICIO 3

"""
    Factorial de un número

    Nota:

    El Factorial de 5, por ejemplo:

    5! = 5 * 4 * 3 * 2 * 1 = 120

    y el de 3:

    3! = 3 * 2 * 1 = 6

    y así para todos..

    PASOS A SEGUIR Y COSAS A TENER EN CUENTA

    Pide por teclado el número del cual quieres calcular el factorial.

    Para que no sea muy grande te recomendamos:

    3,4 o 5 (para hacer las pruebas)

    si ya no lo recuerdas o nunca lo viste, no te preocupes..

    3! es: 3 * 2 * 1 = 6

    4! es: 4 * 3 * 2 * 1 = 24

    5! es: 5 * 4 * 3 * 2 * 1 = 120

    (esto es lo que se pide, en esencia)
"""

# numero = int(input("Factorial del: <3, 4 ó 5> escribe por teclado..: "))
# print(numero)

def factorial(numero):
    listado = np.arange(1, numero + 1).tolist()
    producto = 1

    for i in listado:
        producto = producto * i
    return producto

# Descomentar para ejecutar:
# print(factorial(numero))

# EJERCICIO 4

"""
    Haz un cronómetro en Python:

    Obviamente:

    Horas - Minutos - Segundos

    Debes usar lo siguiente (from time import sleep)

    NOTA: Si quieres puedes usar sleep(0.000001)

    en vez de sleep(1) -> 1 segundo

    (para no esperar 1 segundo a ver los cambios)

    Para poder pararlo en poco tiempo,

    imprime mientras horas<2, cuando llegue a 2 debería parar la ejecución.

    Debería ejecutarse en unos 2 minutos aprox.
"""
# Segundos
segundo = np.arange(0, 60).tolist()
# print(segundo)

# Minutos
minutos = np.arange(0, 60).tolist()
# print(minutos)

# Horas
horas = np.arange(0, 24).tolist()
# print(horas)

def reloj(horas, minutos, segundos):
    print("h m s")
    for h in horas:                          # [0-1-2-3.....23]
        for m in minutos:                    # [0-1-2-3.............59]
            for s in segundos:               # [0-1-2-3.............59]
                if h<2:
                    print(h,m,s)
                    sleep(0.000001)

reloj(horas, minutos, segundo)