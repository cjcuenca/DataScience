# IMPORTACION LIBRERIAS
import math 
 
 # EJERCICIO  1

""" Una población distribuida normalmente tiene una media de 100 y una desviacion estándar de 20.
¿ Cuál es la puntuación Z de una media muestral de 110, tomada de una muestra de tamaño 4? """

µ = 100
s = 20
x = 110
n = 4

SE = round(s/math.sqrt(n),2)

Zscore = (round((x - µ)/ SE, 2))
Zscore

print(f"\nEJERCICIO 1: La desviación standar de la muestra es {SE} y la puntuación Z {Zscore} ")

 # EJERCICIO  2

""" El tiempo medio conocido que se tarda en entregar una pizza es de 22.5 minutos 
con una desviación estándar de 2 minutos. Pedí pizza todas las semanas durante las 
últimas 10 semanas y obtuve un tiempo de 21.5 minutos.
¿Cuál es la probabilidad de obtener este promedio? """

µ = 22.5
s = 2
x = 21.5
n = 10

SE = round(s/math.sqrt(n),2)

Zscore = (round((x - µ)/ SE, 2))

print(f"\nEJERCICIO 2: La desviación standar de la muestra es {SE} y la puntuación Z {Zscore} ")
print("La probabilidad de obtener ese promedio es un 5,59% ")

 # EJERCICIO  3

""" Si sigo pidiendo pizzas por la toda la eternidad. 
¿A qué nivel puedo esperar que se acerque este promedio? """

µ = 22.5
s = 2
x = 21.5
n = 10**10

SE = s/math.sqrt(n)

Zscore = (round((x - µ)/ SE, 2))

print(f"\nEJERCICIO 3: La desviación standar de la muestra es {SE} y la puntuación Z {Zscore} ")
print("lo que indica que la distribución de las medias muestrales será cada vez más normal según aumente el tamaño de la muestra")