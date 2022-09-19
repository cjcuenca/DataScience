import pandas as pd


# EJERCICIO 1

"""
    Decribe una variable con nombre "notas" que tenga el valor -3
    muestra su valor
"""


def note(notas):
    print(notas)

notas = -3

# Descomentar para ejecutar:
# note(notas)

# EJERCICIO 2

"""
    Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida:
    El valor de "s" es "valor de s" y el valor de y es "valor de y"
"""
s = 25
y = 10

def imprimir(s, y):
    print(f'el valor de s es {s} y el valor de y es {y}')
    print('el valor de s es ' + str(s) + ' y el valor de y es ' + str(y))
    print('el valor de s es ', s, ' y el valor de y es ', y)
    print(f'el valor de s es %s y el valor de y es %s' %(s, y))

# Descomentar para ejecutar:
# imprimir(s, y)

# EJERCICIO 3

"""
    Declarar una variable con nombre "name",
    que tenga el valor de Juan "El profesor"
"""

def profesor(name):
    return name

# Descomentar para ejecutar:
# print(profesor("Juan 'El profesor'"))

# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""

def profesor_2(name_1, name_2):
    result = name_1 + " " + name_2
    print(result)

# Descomentar para ejecutar:
# profesor_2("Juan", "'El profesor'")

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""

frase = "no cuentes los días, haz que los días cuenten"

def titulo(frase):
    print(frase.title())

def mayusculas(frase):
    print(frase.upper())

def minusculas(frase):
    print(frase.lower())

# Descomentar para ejecutar:
# titulo(frase)
# mayusculas(frase)
# minusculas(frase)


# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""
x = 26
y = 35

def sumaValores(x, y):
    print(x + y)

def multiplicación(x, y):
    print(x * y)

def operación():
    print(2 + 32 * 10)

def elevado(x, y):
    print(x ** y)
    result = x ** y
    return result

def redondeo(value):
    print(round(value, 2))

def tipo(value):
    print(type(value))

# Descomentar para ejecutar:
# sumaValores(x, y)
# multiplicación(x, y)
# operación()
# value = elevado(3, 9)
# redondeo(value)
# tipo(value)


# EJERCICIO 7

"""
    Saca el valor absoluto de -32
    Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)
"""
z = 32
lista = [3, -6, 4, -10, 2.6666]


def absoluto(z):
    print("absoluto: ", abs(z))

def test(lista):
    print("máximo: ", max(lista))
    print("mínimo: ", min(lista))

# Descomentar para ejecutar:
# absoluto(z)
# test(lista)



# EJERCICIO 8

"""
    Tratar de reemplazar los valores que faltan en este listado --> por un -1
    L = [10, None, 8, 5, None, 20]
    1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores.
    2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])
"""

L = [10, None, 8, 5, None, 20]

def test_1(L):
    L[1] = -1
    L[-2] = -1
    print(L)

def test_2(L):
    df = pd.DataFrame(L, columns=["listado"])
    print(df)

# Descomentar para ejecutar:
# test_1(L)
# test_2(L)