# EJERCICIO 1
""" 
    1) Crea el siguiente programa:

    Una clase de nombre Librería
    Inicia los siguientes atributos: nombre, sección, editorial y año
    Crea una segunda clase con nombre Rosalia que herede la clase librería.
    En esta clase Rosalia, crea una función "result" cuyo resultado sea los datos de los libros.
    declara los Objetos siguientes:
    libro1 --> Oceanarium, Ciencia, Impedimenta, 2021
    libro2 --> 33 Botones, Novela negra, Atlantis, 2022
    libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022

 """
 from encodings import normalize_encoding, search_function


class Libreria:
    def __init__(self, nombre, seccion, editorial, año):
      self.nombre = nombre
      self.seccion = seccion
      self.editorial = editorial
      self.año = año

class Rosalia(Libreria):
    def __str__(self):
       return f"Nomre: {self.nombre} Sección: {self.seccion} Editorial: {self.editorial} Año: {self.año} "

libro1 = Libreria(Oceanarium, Ciencia, Impedimenta, 2021)
libro2 = Libreria(33 Botones, Novela negra, Atlantis, 2022)
libro3 = Libreria(Venganza en Compostela, Historia, Universo de letras, 2022)