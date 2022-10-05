import math

def error_estandar(s, n):
    return s / math.sqrt(n)

def Zscore(µ, se, x):
    return round((x - µ)/ se, 2)

# EJERCICIO 1

"""
    Una población distribuida normalmente tiene una media de 100 y una desviacion estándar de 20.
    ¿ Cuál es la puntuación Z de una media muestral de 110, tomada de una muestra de tamaño 4?
"""

µ = 100
s = 20
x = 110
n = 4

se = error_estandar(s, n)
# print("Error estandar: ", se)

# print("Z score: ", Zscore(µ, se, x))


# EJERCICIO 2

"""
    El tiempo medio conocido que se tarda en entregar una pizza es de 22.5 minutos con una desviación estándar de 2 minutos.
    Pedí pizza todas las semanas durante las últimas 10 semanas y obtuve un tiempo de 21.5 minutos.
    ¿Cuál es la probabilidad de obtener este promedio?
"""
µ = 22.5
s = 2
x = 21.5
n = 10

se = error_estandar(s, n)
# print("Error estandar: ", se)

# print("Z score: ", Zscore(µ, se, x))

# La probabilidad para -1.58 es 0.0571 --> 5.71%


# EJERCICIO 3

# Si sigo pidiendo pizzas por la toda la eternidad. ¿A qué nivel puedo esperar que se acerque este promedio?

"""
    Pediente de revisión
"""

µ = 22.5
s = 2
x = 21.5
n = 2

se = error_estandar(s, n)
# print("Error estandar: ", se)

# print("Z score: ", Zscore(µ, se, x))

# Disminuyendo el tamaño muestral

## Otra opción o interpretación...

µ = 22.5
s = 2
x = 21.5
n = 10**10

se = error_estandar(s, n)
print("Error estandar: ", se)

print("Z score: ", Zscore(µ, se, x))

# Elevando el numero de muestra nos acercaremos a la media
