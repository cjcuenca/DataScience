# EJERCICIO 1

"""
    Crear un pequeño programa que calcule la multiplicación de 2 números (x, y)

    x = 3, y = 5
    x = 7, y = 3
"""

# a) Con una función (por ejemplo funcion_multiplicar)


def funcion_multiplicar(x, y):
    return x * y

# Descomentar para ejecutar:
# print(funcion_multiplicar(3, 5))
# print(funcion_multiplicar(7, 3))

# b) Con la función lambda (Tal vez puedes ir a repasarlo)

# Descomentar para ejecutar:
result = (lambda x, y: x * y)(3, 5)
result = (lambda x, y: x * y)(7, 3)
# print(result)

# otra opción...
# MEJOR OPCIÓN!!
f = lambda x, y: x * y

# Descomentar para ejecutar:
# print(f(3, 5))
# print(f(7, 3))

# otra opción...
def funcion_lambda(x, y):
    return (lambda x, y: x * y)(x, y)

# Descomentar para ejecutar:
# print(funcion_lambda(3, 5))

# c) Realizarlo con entrada de teclado (input)

# Descomentar para ejecutar:
# x = int(input("Escribe un número: "))
# y = int(input("Escribe un número: "))

# print(funcion_multiplicar(x, y))


# EJERCICIO 2

"""
    -A-

        Dado un string:

        "Level"

        ¿Es un palíndromo?
"""
A = "Level"

def palindromo(A):
    A1 = []
    i = -1
    while len(A1) < len(A):
        A1.append(A[i])
        i -= 1
    return A1

# Descomentar para ejecutar:
# print(palindromo(A))

def funcion_comparar(A, A1):
    different = 0
    for i in range(len(A)):
        if A[i] != A1[i]:
            different += 1
    return different

numero_diferente = funcion_comparar(A, palindromo(A))

def funcion_resultado(numero_diferente):
    if numero_diferente == 0:
        print('palindromo')
    else:
        print("No es palindromo")
        print(f"Tenemos {numero_diferente} elementos diferentes")

# Descomentar para ejecutar:
# funcion_resultado(numero_diferente)

"""
    -B-

        ¿Y este string?

        "level"

        Nota: "Es un palíndromo si se invierte el orden del string, el resultado es exactamente el mismo"
"""
B = "level"

# print(palindromo(B))

numero_diferente = funcion_comparar(B, palindromo(B))

# Descomentar para ejecutar:
# funcion_resultado(numero_diferente)


# EJERCICIO 3

"""
    Dado 2 strings:

    S1 = "Hi!"
    S2 = "Hello!"

    Imprimir las letras que son comunes
"""

# Primera Opción

S1 = "Hi!"
S2 = "Hello!"

def comunes(S1, S2):
    list_letras = []
    for elemento in S1:
        for letra in S2:
            if elemento == letra:
                list_letras.append(elemento)
    return list_letras

# print(comunes(S1, S2))

# Segunda opción...

def comunes_2(S1, S2):
    list_letras = []
    for elemento in S1:
        if elemento in S2:
            list_letras.append(elemento)
    return list_letras

# print(comunes_2(S1, S2))

# Tercera opción...

def comunes_3(S1, S2):
    sin_coincidencia = []
    for elemento in S1:
        for letra in S2:
            if elemento == letra and elemento not in sin_coincidencia:
                sin_coincidencia.append(elemento)
    return sin_coincidencia

# print(comunes_3(S1, S2))