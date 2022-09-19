import numpy as np


# EJERCICIO 1

# Crea una matriz con ayuda numpy:

# 1) Cuya matriz contenga 4 filas por 4 columnas de ceros

matriz = np.zeros((4, 4))

# Descomentar para ejecutar:
# print(matriz)

# 2) Apartir de la matriz de ceros crea la matriz identidad

def identidad(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == i:
                matriz[i][j] = 1
    return matriz

# Descomentar para ejecutar:
# print(identidad(matriz))




# EJERCICIO 2

# Crea una matriz con ayuda numpy:

# Primera fila contenga: 3, 6, 8
# Segunda fila contenga: 20, 5, 7
# Tercera fila contenga: 10, 14, 1

B = np.array([
    [3, 6, 8],
    [20, 5, 7],
    [10, 14, 1]
])

# Descomentar para ejecutar:
# print(B)
# print(type(B))

# 1) Crea la transpuesta de esta matriz

# Descomentar para ejecutar:

# Una forma...
# print(B.T)

# Otra forma...
# print(np.transpose(B))


# 2) Muestra el tamaño de la matriz

# Descomentar para ejecutar:
# print(B.size)


# 3) Muestra las dimensiones

# Descomentar para ejecutar:
# print(B.shape)

# 4) ¿La matriz tiene valores menores de 0?

def menores_0(matriz):
    return np.all(matriz < 0)

# Descomentar para ejecutar:
# print(menores_0(B))

# 5) ¿La matriz tiene algún valor mayor de 10?

def mayor_10(matriz):
    return np.any(matriz > 10)

# Descomentar para ejecutar:
# print(mayor_10(B))

# 6) Coge una muestra de 5 valores de esa matriz usando linspace

def muestra(matriz):
    return np.linspace(matriz.min(), matriz.max(), 5)

# Descomentar para ejecutar:
# print(muestra(B))

# 7) La matriz contiene el valor 7

def comprobar(matriz):
    return 7 in matriz

# Descomentar para ejecutar:
# print(comprobar(B))

# 8) Crea una copia de esa matriz en una única dimensión

def unica(matriz):
    return matriz.flatten()

# Descomentar para ejecutar:
# print(unica(B))

matriz_2 = unica(B)

# 9) Crea una copia de esa matriz en una única dimensión, en este caso usando un bucle y una lista vacia

def unica_2(matriz):
    lista_final = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            lista_final.append(matriz[i][j])
    return np.array(lista_final)

# Descomentar para ejecutar:
# print(unica_2(B))

# 10) Realiza a esta última matriz creada con flatten la potencia de 3
# print(matriz_2)

# Descomentar para ejecutar:
# print(pow(matriz_2, 3))