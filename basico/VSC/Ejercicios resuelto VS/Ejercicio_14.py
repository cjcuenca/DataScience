import pandas as pd

# EJERCICIO 1

"""
    Cada número es la suma de los 2 anteriores:

    0-1-1-2-3-5-8-13-21-34...

    Se pide programar esa secuencia con Python.

    Nota:

    Apendiza elementos hasta tener 10 primeros resultados.

    (los 10 números indicados desde 0 hasta 34)

    Si sabes, hazlo de varias formas diferentes
"""

def fibonacci(limite):
    L = [0, 1]
    while (len(L) < limite):
        L.append(L[-1] + L[-2])
    return L 

# Descomentar para ejecutar:
# print(fibonacci(10))



# EJERCICIO 2

# Cada número es la suma de los 2 anteriores:

# 0-1-1-2-3-5-8-13-21-34...

# Se pide programar para los números de fibonacci mayores de 1000

# Primero muestra los valores de 0 hasta 1000000, crea una lista
# con ese listado crea una segunda lista con los mayores de 1000

fibo = fibonacci(50)

# Descomentar para ejecutar:
# print(fibo)

def filtrado(minimo, lista):
    mayores_1000 = []
    for i in lista:
        if i > minimo:
            mayores_1000.append(i)
    return mayores_1000

# Descomentar para ejecutar:
# print(filtrado(1000, fibo))



# EJERCICIO 3

# Se pide crear un NUEVO dataframe para cada uno de los siguientes casos

# planteados y que están relacionados con el Titanic DataSet

# (antes debéis de cargar el archivo como df)

# 1) Leer el archivo train.csv del titanic dataset

df = pd.read_csv("./src/train.csv")

# Descomentar para ejecutar:
# print(df)

# 2) Crear un dataframe de nombre df_sobreviven refiriéndose a un dataframe en el que todos los pasajeros sobreviven

    # NOTA: si al principio no estás seguro del resultado, puedes usar value_counts() para comprobar tu resultado

def supervivencia(df, valor):
    return df[df["Survived"] == valor]

df_sobreviven = supervivencia(df, 1)

# Descomentar para ejecutar:
# print(df_sobreviven)

# Descomentar para ejecutar:
# Dos formas de comprobar los valores
# print(df_sobreviven.Survived.value_counts())
# print(len(df_sobreviven))

# print(f"Numero de pasajeros que sobreviven {len(df_sobreviven)}")

# 3) Crear un dataframe de nombre df_no_sobreviven refiriéndose a un dataframe en el que NINGUNO de los pasajeros sobrevive

df_no_sobreviven = supervivencia(df, 0)

# Descomentar para ejecutar:
# print(df_no_sobreviven)

# Descomentar para ejecutar:
# Dos formas de comprobar los valores
# print(df_no_sobreviven.Survived.value_counts())
# print(len(df_no_sobreviven))

# print(f"Numero de pasajeros que NO sobreviven {len(df_no_sobreviven)}")

# 4) DataFrame de hombres que no sobrevivieron en el titanic

def filtrado_sexo(df, sexo):
    return df[df["Sex"] == sexo]

# Descomentar para ejecutar:
# print(filtrado_sexo(df_no_sobreviven, "male"))
# print("Número de Hombre que NO sobrevivieron %s" % (len(filtrado_sexo(df_no_sobreviven, "male"))))

# 5) DataFrame de hombres que si sobrevivieron en el titanic

# Descomentar para ejecutar:
# print(filtrado_sexo(df_sobreviven, "male"))
# print("Número de Hombre que sobrevivieron %s" % (len(filtrado_sexo(df_sobreviven, "male"))))

# 6) DataFrame de mujeres que no sobrevivieron en el titanic

# Descomentar para ejecutar:
# print(filtrado_sexo(df_no_sobreviven, "female"))
# print("Número de Mujeres que NO sobrevivieron %s" % (len(filtrado_sexo(df_no_sobreviven, "female"))))

# 7) DataFrame de mujeres que si sobrevivieron en el titanic

# Descomentar para ejecutar:
# print(filtrado_sexo(df_sobreviven, "female"))
# print("Número de Mujeres que sobrevivieron %s" % (len(filtrado_sexo(df_sobreviven, "female"))))