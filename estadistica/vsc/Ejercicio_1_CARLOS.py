    # EJERCICIO 1
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

# Dada estos valores: 15 16 17 16 21 22 15 16 15 17 16 22 14 13 14 14 15 15 14 15 16 10 19 15 15 22 24 25 15 16
# Creamos un dataframe que usaremos para realizar los gráficos
df = pd.DataFrame({"x": [15, 16, 17, 16, 21, 22, 15, 16, 15, 
                        17, 16, 22, 14, 13, 14, 14, 15, 15, 
                        14, 15, 16, 10, 19, 15, 15, 22, 24, 
                        25, 15, 16]})

# 1) Realiza un Histograma con tamaño de barra 2.

def histograma(df):
    plt.hist(df.x, bins=2, color="green",
             histtype="bar", rwidth=0.25)
    plt.grid(True)
    plt.xlabel("Datos")
    plt.ylabel("Frecuencia")
    plt.title("Ejercicio 1.1")
    plt.show()

#histograma(df)

# 2) ¿Cuál es el número que más se repite?

#print(df.x.value_counts())
#print(df.x.mode())
# Por gráfica se muestra que el numero que más frecuencia hay está entre el 13 y 14, 
# mientras que el que se puestra por value_counts o por mode se ve que es el 15

# 3) ¿Qué pasa si cambiamos a tamaño de barra 5?

def histograma(df):
    plt.hist(df.x, bins=5, color="green",
             histtype="bar", rwidth=0.25)
    plt.grid(True)
    plt.xlabel("Datos")
    plt.ylabel("Frecuencia")
    plt.title("Ejercicio 1.3")
    plt.show()

#histograma(df)

# Parece que el que más frecuente se encuentra entre 14 y 15

# 4) ¿Qué pasa si cambiamos a tamaño de barra 20?

def histograma(df):
    plt.hist(df.x, bins=20, color="green",
             histtype="bar", rwidth=0.25)
    plt.grid(True)
    plt.xlabel("Datos")
    plt.ylabel("Frecuencia")
    plt.title("Ejercicio 1.4")
    plt.show()

histograma(df)

# Parece que el numero más frecuente es el 15

# 5) ¿Qué parece indicar el sesgo en la distribución?
# Parece que hay un sesgo positivo 
