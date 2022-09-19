"""
    Basándote en la teoría explicada en clase sobre Python
    realiza los siguientes ejercicios
"""

# EJERCICIO 1

"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, caracter):
    return n * caracter

# Descomentar para ejecutar:
# print("1) generar_n_caracteres", generar_n_caracteres(5, 'x'))

# EJERCICIO 2

"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
"""

def procedimiento(lista):
    for i in lista:
        print(i * "x")

# Descomentar para ejecutar:
# procedimiento([4, 9, 7])

# EJERCICIO 3

"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga

# Descomentar para ejecutar:
# print(mas_larga(["coche", "tortuga", "bici"]))

# Otra opción contando caracteres...

diccionario = {}

def numero_letras(lista, diccionario):
    for palabra in lista:
        contador = 0
        for letra in palabra:
            contador += 1
        diccionario[palabra] = contador
    return diccionario

# Descomentar para ejecutar:
# print(numero_letras(["coche", "tortuga", "bici"], diccionario))
# print(max(diccionario))

# EJERCICIO 4

"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista, n):
    listado = []
    for i in lista:
        if len(i) > n:
            listado.append(i)
    return listado

# Descomentar para ejecutar:
# print(filtrar_palabras(["coche", "tortuga", "bici"], 4))

# EJERCICIO 5

"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def c_mayusculas(cadena):
    cont = 0
    for i in cadena:
        if i != i.lower(): #Recordar que lower() convierte una cadena en minúsculas
            cont += 1
    return "La cadena tiene", cont, "mayuscula/s"

# Descomentar para ejecutar:
# print(c_mayusculas("Mas que Coches"))

# EJERCICIO 6

"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a 20.
"""

def mayores(tup):
    cont = 0
    for i in tup:
        if i > 20:
            cont += 1
    return "Hay", cont, "numeros mayores a 20"

# Descomentar para ejecutar:
# print(mayores((15, 20, 16, 31, 40, 50, 11, 13, 48, 60)))

# EJERCICIO 7

"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

def main():
    x = int(input("Cuantos nombres quieres ingresar?: "))
    lista = []
    for i in range(x):
        a = input("Ingresa el nombre: ")
        lista.append(a)
    print("\n")

    comienzo = input("Con que letra empieza el nombre?: ")
    cont = 0
    for i in lista:
        if i[0] == comienzo.lower() or i[0] == comienzo.upper() :
            cont += 1
    return cont

# Descomentar para ejecutar:
# print(main())

# EJERCICIO 8

"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""

def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"

    for x in vocales:
        contador = 0
        for i in cadena:
            if i == x:
                contador += 1
        print("Hay %d %s." % (contador, x))

# Descomentar para ejecutar:
# contar_vocales("Hola Mundo")
