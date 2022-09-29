# EJERCICIO 1
""" En 2007-2008, la altura promedio de un jugador de baloncesto profesional fue de 2,00 metros
    con una desviación estándar de 0,02 metros. Harrison Barnes es un jugador de baloncesto que mide 2,03 metros. 
    ¿Qué porcentaje de jugadores son más altos que Barnes?
 """
µ = 2.00 
s = 0.02
x = 2.03

def calculo_desviaciones(x, s, µ):
    return (round((x - µ)/ s, 2))

Zscore = calculo_desviaciones(x, s, µ)
print(f"EJERCICIO 1 - Desviación estandar de Barnes es: {Zscore} que corresponde a un 93,32% en la tabla Z")

porcentaje_mas_altos = round(100 - 92.32, 2)
print(f"Un {porcentaje_mas_altos}% de jugadores son más altos que Barnes")

# EJERCICIO 2
""" Chris Paul mide 1,83 metros. ¿Qué proporción de jugadores de baloncesto se encuentran 
 entre las alturas de Paul y Barnes?
"""

µ = 2.00 
s = 0.02
x = 1.83

Zscore_Chris = calculo_desviaciones(x, s, µ)
print(f"EJERCICIO 2 - Desviación estandar de Chris Paul es: {Zscore_Chris} que corresponde a un practivamente un 0% en la tabla Z")
print(f"Por tanto la proporción de jugadores de baloncesto que se encuentran entre las alturas de Paul y Barnes es de 93,32% ")

# EJERCICIO 3
""" El 92 % de los candidatos obtuvo una puntuación tan buena o peor que la de Steve. 
 Si el puntuación promedio fue 55 con una desviación estándar de 6 puntos, ¿cuál fue el puntuación de Steve? 
"""
µ = 55 
s = 6
Zscore = 1.41  #Un 92% en la tabla z significa un Zscore de 1.41

x = round((Zscore*s + µ), 2)

print(f"EJERCICIO 3 - La puntación de Steve es de: {x}")
