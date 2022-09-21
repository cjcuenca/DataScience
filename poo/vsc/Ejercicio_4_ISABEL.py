# EJERCICIO 1

"""
    Crea una clase persona. Sus atributos deben ser su nombre y su edad.
    Además crea un método cumpleaños, que aumente en 1 la edad de la persona.
"""

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad +=  1
        return self.edad

p = Persona("Isabel", 10)

# Descomentar para ejecutar:
# print("La edad es: ", p.cumpleaños(), " años")


# EJERCICIO 2

"""
    Para la clase anterior definir el método str.
    Debe retornar al menos el nombre de la persona.
"""

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad +=  1
        return self.edad

    def __str__(self):
        return "Persona: " + self.nombre

p = Persona("Isabel", 10)

# Descomentar para ejecutar:
# print(p)

# EJERCICIO 3

"""
    Extender la clase persona agregando un atributo saldo y un método transferencia(self, persona2, monto).
    El saldo representa el dinero que tiene la persona.
    El método transferencia hace que la Persona que llama el método le transfiera la cantidad monto al objeto persona2.
    Si no tiene el dinero suficiente no se ejecuta la acción.
"""

class Persona:

    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo

    def cumpleaños(self):
        self.edad +=  1
        return self.edad

    def __str__(self):
        return "Persona: " + self.nombre

    def transferencia(self, persona, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            persona.saldo += monto
            return "Transferencia ok!"
        else:
            return "No se puede efectuar la transferencia"

p = Persona("Isabel", 10, 2)
p2 = Persona("Pedro", 20, 20)

# Descomentar para ejecutar:
# print(p2.transferencia(p, 7))