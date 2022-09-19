# EJERCICIO 1

"""
    Dado este listado de números:

    -3, 150, 0, 499, 500, 1200, -350, 0, 750, 25

    Haz un pequeño algoritmo que haga lo siguiente:

    Si el número es negativo debe imprimir lo siguiente el valor es negativo
    Si es 0 debe imprimir un mensaje que indique: 0
    Si se encuentra entre 0 (no incluido) y 200 (si incluido), imprime 0,200
    Si se encuentra entre 200 (no incluido) y 500 (no incluido), debe imprimir (200, 500)
    Si es 500 debe continuar sin hacer nada
    Si se encuentra entre 500 (no incluido) y 1000 (no incluido) debe saltar automaticamente y dejar de testear (parar)
    Para el resto de números, debe decir: valor demasiado grande, desde 1000, en adelante

"""

valores = [-3, 150, 0, 499, 500, 1200, -350, 0, 750, 25]


# 1) Escribir en formato lista

# Descomentar para ejecutar:
# print(valores)

# 2) Haz el propio ejercicio de programación planteado

def comprobar(lista):
    for numero in lista:
        if numero < 0:
            print(f"{numero} es negativo")
        elif numero == 0:
            print(f"{numero} es neutro (0)")
        elif 0 < numero <= 200:
            print(f"{numero} está entre 0,200")
        elif 200 < numero < 500:
            print(f"{numero} está entre 200,500")
        elif numero == 500:
            continue
        elif 500 < numero < 1000:
            print(f"{numero} está entre 500, 1000 paramos código")
            break
        else:
            print(f"{numero} es demasiado grande")

# Descomentar para ejecutar:
# comprobar(valores)


# EJERCICIO 2

# Dada la lista de nombre "listado" y de valores: 10, 20, 20, 30, 40, 40, 40

# 1) Crea la lista e imprimela

listado = [10, 20, 20, 30, 40, 40, 40]

# Descomentar para ejecutar:
# print(listado)

# 2) Haz un set de esa lista

# Descomentar para ejecutar:
# print(set(listado))

# 3) Trata de buscar los números NO REPETIDOS de esa lista (sin usar set)
    # Pista: Puedes almacenar todo en una nueva lista

def no_repetidos(lista):
    unicos = []
    for numero in lista:
        if numero not in unicos:
            unicos.append(numero)
    return unicos

# Descomentar para ejecutar:
# print(no_repetidos(listado))


# EJERCICIO 3

# Dados estos clientes:

# Usando el continue/break

# Trata de averiguar si un cliente concreto se encuentra en la BBDD (Base de Datos)

# "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"

clientes = ["Ana Pérez", "Juan García", "Andres Álvarez",
            "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez",
            "Alberto Delgado", "Susana Castro", "Luis González"]

# print(clientes)

usuario = "Alberto Delgado"

def buscar(clientes, usuario):
    for cliente in clientes:
        cliente_1 = cliente.lower()
        usuario_1 = usuario.lower()
        if cliente_1 == usuario_1:
            return f"'{usuario}' está en nuestra base de datos"
    return f"'{usuario}' NO está en nuestra base de datos"

# Descomentar para ejecutar:
# print(buscar(clientes, usuario))