
# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos números y devuelva el mayor de ellos.
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""


def maximo(n1, n2):
    if n1 < n2:
        print(f"El valor máximo es {n2}")
        return n2
    elif n2 < n1:
        print(f"El valor máximo es {n1}")
        return n1
    else:
        return "son iguales"

# Descomentar para ejecutar:
# print(maximo(8, 5))


# EJERCICIO 2

"""
    Definir una función max_de_tres(),
    que tome tres números como argumentos y
    devuelva el mayor de ellos.
"""


def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    else:
        return "Son iguales"

# Descomentar para ejecutar:
# print(max_de_tres(8, 5, 9))

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista
    o una cadena dada.
    (Es cierto que python tiene la función len() incorporada,
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""


def largo_cadena(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

# Descomentar para ejecutar:
# print(largo_cadena("hola mundo"))
# print(largo_cadena([25, 30]))
# print("len: ", len([25, 30]))

# EJERCICIO 4


"""
    Escribir una función que tome un carácter y devuelva True si es una vocal,
    de lo contrario devuelve False.
"""

def es_vocal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False

# Descomentar para ejecutar:
# print("Es vocal: ", es_vocal("a"))
# print("Es consonante: ", es_vocal("b"))

# otra opción...

def es_vocal_1(x):
    x = x.lower()
    listado_comparacion = ["a", "e", "i", "o", "u"]
    if x in listado_comparacion:
        return True
    return False

# Descomentar para ejecutar:
# print("Es vocal: ", es_vocal_1("A"))
# print("Es vocal: ", es_vocal_1("a"))
# print("Es consonante: ", es_vocal_1("b"))

# EJERCICIO 5

"""
    Escribir una función suma() y una función multip() que sumen y multipliquen
    respectivamente todos los números de una lista.
    Por ejemplo: suma([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
def suma(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def multip(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

# Descomentar para ejecutar:
# print("suma: ", suma([8, 5]))
# print("multiplicacion: ", multip([8, 5]))

print("Enhorabuena acabaste los ejercicios")