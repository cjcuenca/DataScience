import pandas as pd
import matplotlib.pyplot as plt

# Creamos un dataframe que luego usaremos para mostrar los datos:

df = pd.DataFrame({"x": [10, 20, 30, 40, 50],
                   "y": [15, 5, 10, 8, 6]})

def lineas(df):
    df.plot()
    plt.show()

# lineas(df)

def barras(df):
    df.plot(kind="bar") #, color=["blue", "green", "red", "orange"])
    plt.show()

# barras(df)

def apilado(df):
    df.plot(kind="bar", stacked=True,
            grid=True, title="Gráfica ejemplo con Pandas")
    plt.show()

# apilado(df)

# barras(df.y.value_counts())