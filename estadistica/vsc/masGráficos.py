import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

# Creamos un dataframe que usaremos para realizar los gráficos
df = pd.DataFrame({"x": [1,32,4,23,40,2,2,27,6,18,49,67,46,7,
                         20,24,35,33,40,80,26,85,77,11,92,24],
                   "y": [31,10,85,25,4,83,32,43,66,18,93,6,42,
                         27,21,42,53,32,85,32,42,58,67,17,4,5]})

# HISTOGRAMAS:

def histograma(df):
    plt.hist(df.y)
    plt.grid(True)
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Mi primer Histograma")
    plt.show()

# histograma(df)

def histograma_2(df):
    plt.hist(df.y, bins=10, color="green",
             histtype="bar", rwidth=0.25)
    plt.grid(True)
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Mi primer Histograma")
    plt.show()

# histograma_2(df)

# SCATTER PLOT - nubes de puntos -

def scatterPlot(df):
    plt.scatter(df.x, df.y, label="años", marker="+", s=200)
    plt.grid(True)
    plt.xlabel("eje X")
    plt.ylabel("Eje y")
    plt.title("nube de puntos")
    plt.legend()
    plt.show()

# scatterPlot(df)

# PIE CHART - graficos circulares -

df_2 = pd.DataFrame({"x": [4, 2, 4, 1],
                     "y":["Futbol", 'Baloncesto', 'Gimnasio', 'TV']})

def pieChart(df_2):
    plt.title("Horas semanales de tiempo libre")
    plt.pie(df_2.x, labels=df_2.y, colors=["r", "y", "g", "b"],
            startangle=90, radius=1.0, autopct="%1.2f%%")
    plt.show()

# pieChart(df_2)

# GRAFICO 3D

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 4, 4, 2, 4, 5, 2, 3, 5, 6]
z = [3, 3, 3, 3, 5, 5, 2, 4, 7, 8]

def grafico_3d(x, y, z):
    ax = plt.axes(projection="3d")
    ax.scatter3D(x, y, z, marker="o", s=100)
    plt.show()

# grafico_3d(x, y, z)
