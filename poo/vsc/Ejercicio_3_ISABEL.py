# EJERCICIO 1

"""
    Crearemos una clase llamada NumeroComplejo.
    Este tipo tiene un atributo x para la coordenada en x e y para la coordenada en y.
    Representa un número complejo de la forma (x, y).
"""

class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

nc = NumeroComplejo(1, 2)

# Descomentar para ejecutar:
# print(nc.x)


# EJERCICIO 2

"""
    Ahora defina dentro de la clase NumeroComplejo un función imprimir
    donde muestre los valores de x e y.
"""


class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        return f"El valor de x es {self.x} y el valor de y es {self.y}"

nc = NumeroComplejo(1, 2)

# Descomentar para ejecutar:
# print(nc.imprimir())

# EJERCICIO 3

"""
    Define la función str para la clase NumeroComplejo
    para poder imprimir usando la función print.
"""

class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        return f"El valor de x es {self.x} y el valor de y es {self.y}"

    def __str__(self):
        s = str(self.x) + ", " + str(self.y)
        return s

nc = NumeroComplejo(1, 2)

# Descomentar para ejecutar:
# print(nc)


# EJERCICIO 4

"""
    Define una función que compara dos números complejos,
    ya que si dos objetos distintos tienen sus atributos iguales,y
    sino NO se consideran iguales.
"""


class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        return f"El valor de x es {self.x} y el valor de y es {self.y}"

    def __str__(self):
        s = str(self.x) + ", " + str(self.y)
        return s

    def son_iguales(self, c2):
        if self.x == c2.x and self.y == c2.y:
            return True
        return False

nc1 = NumeroComplejo(1, 2)
nc2 = NumeroComplejo(1, 6)

# Descomentar para ejecutar:
# print(nc1.son_iguales(nc2))

# EJERCICIO 5

"""
    Realiza un método que sume dos numeros complejos sin modificiar los objetos originales,
    ya que se retorna un nuevo numero NumeroComplejo.
"""

class NumeroComplejo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        return f"El valor de x es {self.x} y el valor de y es {self.y}"

    def __str__(self):
        s = str(self.x) + ", " + str(self.y)
        return s

    def son_iguales(self, c2):
        if self.x == c2.x and self.y == c2.y:
            return True
        return False

    def sumar_complejos(self, c2):
        a = self.x + c2.x
        b = self.y + c2.y
        return NumeroComplejo(a, b)

nc1 = NumeroComplejo(1, 2)
nc2 = NumeroComplejo(1, 6)

# Descomentar para ejecutar:
r = nc1.sumar_complejos(nc2)
# print(r)