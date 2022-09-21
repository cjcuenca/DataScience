# EJERCICIO 1

"""
    Crearemos una clase llamada NumeroComplejo.
    Este tipo tiene un atributo x para la coordenada en x e y para la coordenada en y.
    Representa un número complejo de la forma (x, y).
"""

class NumeroComplejo():
    def __init__(self,x,y):
        self.x = x 
        self.y = y 

#numerocomplejo1 = NumeroComplejo(3,5)

# EJERCICIO 2

"""
    Ahora defina dentro de la clase NumeroComplejo un función imprimir
    donde muestre los valores de x e y.
"""
class NumeroComplejo:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    
    def imprimir(self):
        return f"({self.x},{self.y})"

#numerocomplejo1 = NumeroComplejo(3,5)
#print(numerocomplejo1.imprimir())

# EJERCICIO 3

"""
    Define la función str para la clase NumeroComplejo
    para poder imprimir usando la función print.
"""
class NumeroComplejo():
    def __init__(self,x,y):
        self.x = x 
        self.y = y 

    def __str__(self):
        return  f"({self.x},{self.y})"

# print(NumeroComplejo(3,5))


# EJERCICIO 4

"""
    Define una función que compara dos números complejos,
    ya que si dos objetos distintos tienen sus atributos iguales,y
    sino NO se consideran iguales.
"""
class NumeroComplejo():
    def __init__(self,x,y):
        self.x = x 
        self.y = y 

    def __str__(self):
        return  f"({self.x},{self.y})"

    def numeros_complejos_iguales(self,numero):
        return self.x == numero.x and self.y == numero.y 

# numerocomplejo1 = NumeroComplejo(3,4)
# numerocomplejo2 = NumeroComplejo(3,4)

# if numerocomplejo1.numeros_complejos_iguales(numerocomplejo2):
#    print(f"({numerocomplejo1.x},{numerocomplejo1.y}) y ({numerocomplejo2.x},{numerocomplejo2.y}) son iguales")
# else:
#    print(f"({numerocomplejo1.x},{numerocomplejo1.y}) y ({numerocomplejo2.x},{numerocomplejo2.y}) NO Son iguales")

# EJERCICIO 5

"""
    Realiza un método que sume dos numeros complejos sin modificiar los objetos originales,
    ya que se retorna un nuevo numero NumeroComplejo.
"""

class NumeroComplejo():
    def __init__(self,x,y):
        self.x = x 
        self.y = y 

    def __str__(self):
        return  f"({self.x},{self.y})"

    def suma_numeros_complejos(self,numero):
        suma_numeros_complejos.x=self.x+numero.x
        suma_numeros_complejos.y=self.y+numero.y
        return suma_numeros_complejos

numerocomplejo1 = NumeroComplejo(3,5)
numerocomplejo2 = NumeroComplejo(3,4)

suma_numeros_complejos = NumeroComplejo(0,0)

suma_numeros_complejos = numerocomplejo1.suma_numeros_complejos(numerocomplejo2)

print(suma_numeros_complejos)
