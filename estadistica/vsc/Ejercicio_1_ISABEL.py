import matplotlib.pyplot as plt
import pandas as pd

# EJERCICIO 1

# Dada estos valores: 15 16 17 16 21 22 15 16 15 17 16 22 14 13 14 14 15 15 14 15 16 10 19 15 15 22 24 25 15 16

df = pd.DataFrame({"Data":  [15, 16, 17, 16, 21, 22, 15, 16, 15,
                            17, 16, 22, 14, 13, 14, 14, 15, 15,
                            14, 15, 16, 10, 19, 15, 15, 22, 24,
                            25, 15, 16,]})

# 1) Realiza un Histograma con tamaño de barra 2.

def histograma(df, bin):
    plt.hist(df.Data, bins=bin, color="green",
             histtype="bar", rwidth=0.25)
    plt.grid(True)
    plt.xlabel("Datos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma con barra 2")

    plt.show()

# histograma(df, 2)

# 2) ¿Cuál es el número que más se repite?

# El valor 14 es el que más se repite

# 3) ¿Qué pasa si cambiamos a tamaño de barra 5?

# histograma(df, 5)

# 4) ¿Qué pasa si cambiamos a tamaño de barra 20?

# histograma(df, 20)

# 5) ¿Qué parece indicar el sesgo en la distribución?

# Tiene un sesgo positivo con valores atípicos a la derecha.