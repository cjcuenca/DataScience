import pandas as pd

# EJERCICIO 1


# 1) Crea una lista de nombre "Concursante" que contenga los siguientes valores:
    # "Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"

Concursante = ["Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"]

# Descomentar para ejecutar:
# print(Concursante)

# 2) Crea una lista de nombre "Resultados" que contenga los siguientes valores:
    # 20, 30, 50, 20, 10, 5, 60, 40

Resultados = [20, 30, 50, 20, 10, 5, 60, 40]

# Descomentar para ejecutar:
# print(Resultados)

# 3) Crea un diccionario con los concursantes y los resultados.

data = {"Concursantes": Concursante, "Resultados": Resultados}

# Descomentar para ejecutar:
# print(data)

# 4) Crea un dataframe vacio y apendiza los concursantes y los resultados mediante el empleo de un bucle for

def create_df(data):
    df = pd.DataFrame(columns=["Concursantes", "Resultados"])
    for key, value in data.items():
        df[key] = value
    return df

# Descomentar para ejecutar:
# print(create_df(data))

df = create_df(data)

# 5) Con ayuda de loc filtra los resultados obtenidos desde Pedro hasta Lara.

# Descomentar para ejecutar:
# print(df.loc[1:5, :])

# 6) Con ayuda de loc filtra los resultados obtenidos mayores o iguales a 40

# Descomentar para ejecutar:
# print(df[df["Resultados"] >= 40])

# 7) Muestra el concursante con la mayor puntuación

# Descomentar para ejecutar:
# print(df["Resultados"].max())

# 8) Muestra el concursante con la menor puntuación

# Descomentar para ejecutar:
# print(df["Resultados"].min())

# 9) Modifica con la ayuda de loc los valores 20 por 0

df.loc[df["Resultados"] == 20, "Resultados"] = 0

# Descomentar para ejecutar:
# print(df)

# 10) Modifica Concursante "Juan" su puntuación por "None" con ayuda de .loc

df.loc[df["Concursantes"] == "Juan", "Resultados"] = None

# Descomentar para ejecutar:
# print(df)

# EJERCICIO 2 (3)

"""
    Escribe un programa que pida dos palabras y diga si riman o no.
    Si coinciden las tres últimas letras tiene que decir que riman.
    Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
"""
# Descomentar para ejecutar:
# palabra_1 = input("Dime la primera palabra: ")
# palabra_2 = input("Dime la segunda palabra: ")

def rimas(palabra_1, palabra_2):
    if len(palabra_1) < 3 or len(palabra_2) < 3:
        print("Las palabras tiene menos de 3 letras")
    elif palabra_1.endswith(palabra_2[-3:]):
        print("Las palabras Riman")
    elif palabra_1.endswith(palabra_2[-2:]):
        print("Las palabras Riman POCO")
    else:
        print("No rima")

# Descomentar para ejecutar:
# rimas(palabra_1, palabra_2)