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
class Libreria:
  def __init__(self, nombre, seccion, editorial, anio):
    self.nombre = nombre
    self.seccion = seccion
    self.editorial = editorial
    self.anio = anio

class Rosalia(Libreria):
    def result(self):
        #print("Nombre :",self.nombre)
        #print("Seccion :",self.seccion)
        #print("Editorial :",self.editorial)
        #print("Año :",self.anio)

        return f"Nombre : {self.nombre} \n"+\
               f"Seccion : {self.seccion} \n" +\
               f"Editorial : {self.editorial} \n" +\
               f"Año : {self.anio}"

        #return f"La información del libro es {self.nombre} de la Sección: {self.seccion}, de la Editorial: {self.editorial} y del año: {self.anio} "

libro1 = Rosalia("Oceanarium", "Ciencia", "Impedimenta", 2021)
libro2 = Rosalia("33 Botones", "Novela negra", "Atlantis", 2022)
libro3 = Rosalia("Venganza en Compostela", "Historia", "Universo de letras", 2022)

#print(libro1.result())

#Rosalia.result(libro1)

#libro1.result()


# EJERCICIO 2
"""
    2) Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase,
    define una función de nombre misLibros, cuyo resultado sea los datos de los libros:

    libro4 --> Mi primera Novela, Novela, Bruño, 2019
    libro5 --> Gatos, Literatura, Listado, 2018
"""
class MiLibro(Rosalia):
    def misLibros(self):
        if self==libro4 or self==libro5:
            print("Nombre :",self.nombre)
            print("Seccion :",self.seccion)
            print("Editorial :",self.editorial)
            print("Año :",self.anio)
        else:
            print(" NO es mi libro")
       
            
libro4 = Rosalia("Mi primera Novela", "Novela", "Bruño", 2019)
libro5 = Rosalia("Gatos", "Literatura", "Listado", 2018)

#libro4.result()

#MiLibro.misLibros(libro5)

#MiLibro.misLibros(libro1)

#    Realiza la media de los años de los libros 4 y 5

from statistics import mean

L = (libro4.anio,libro5.anio)

print("La media de años es: " ,mean(L))