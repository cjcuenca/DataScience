# Ejercicio 1

"""
    Definir una función inversa() que calcule la inversion de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
"""

def inversa(cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

# Descomentar para ejecutar:
# print("Primera opción inversa: ", inversa("Hola mundo"))

# Otra opción..

def inversa2(cadena):
    return cadena[::-1]

resultado = inversa2("Hola mundo2")

# Descomentar para ejecutar:
# print("Segunda opción inversa: ", resultado)



# Ejercicio 2

"""
    Definir una funcion es_palindromo() que reconoce palindromo
    palabras  que tiene el mismo aspecto escritas invertidas), ejemplo: es_palindromo("radar")
    tendría que devolver True.
"""

def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False

# cadena = input("introduce una letra por favor: ")

# Descomentar para ejecutar:
# print(palindromo(cadena))

# otra opción...
def es_palindromo(cadena):
    palabra_invertida = inversa(cadena)
    indice = 0
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            print("No es palindromo")
            break
    if cont == len(cadena): #Si el contador = a la cantidad de letras de la cadena
        print("Es palindromo") # es porque recorrió todo el ciclo for y todas las
                                            # letras son iguales

# Descomentar para ejecutar:
# es_palindromo(cadena)

# Ejercicio 3

"""
    Definir una funcion superposicion() que tome dos listas y devuelva True si tiene al
    menos 1 elemento en común o devuelva False en caso contrario. Escribe la función usando el bucle for 
    aninado.
"""

# Una opción...
# def superposicion (lista1, lista2):
#     for i in lista1:
#         for x in lista2:
#             if i == x:
#                 return True
#     return False


# opcion más corta...
def superposicion(lista1, lista2):
    for i in lista1:
        if i in lista2:
            return True
    return False

lista1 = [1, 2, 3]
lista2 = [1, 4, 8]

# Descomentar para ejecutar:
# print("Resultado superposicion 1: ", superposicion(lista1, lista2))

lista1 = [0, 2, 3]
lista2 = [1, 4, 8]

# Descomentar para ejecutar:
# print("Resultado superposicion 2: ", superposicion(lista1, lista2))