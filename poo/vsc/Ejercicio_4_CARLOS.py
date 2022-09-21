# EJERCICIO 1

"""
    Crea una clase persona. Sus atributos deben ser su nombre y su edad.
    Además crea un método cumpleaños, que aumente en 1 la edad de la persona.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumple(self):
        self.edad = self.edad + 1
        return self.edad

# Per1=Persona("Pepe", 25)
# Per1.cumple()
# print(Per1.edad)

# EJERCICIO 2

"""
    Para la clase anterior definir el método str.
    Debe retornar al menos el nombre de la persona.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"El cliente: {self.nombre} tiene: {self.edad} "   

    def cumple(self):
        self.edad = self.edad + 1
        return self.edad

# Persona1=Persona("Pepe", 25)

# print(Persona1)

# EJERCICIO 3

"""
    Extender la clase persona agregando un atributo saldo 
    y un método transferencia(self, persona2, monto).
    El saldo representa el dinero que tiene la persona.
    El método transferencia hace que la Persona que llama el método le transfiera la cantidad 
    monto al objeto persona2.
    Si no tiene el dinero suficiente no se ejecuta la acción.
"""
class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo

    def __str__(self):
        return f"El cliente: {self.nombre} tiene: {self.edad} y el saldo en cuenta es: {self.saldo}"   

    def cumple(self):
        self.edad = self.edad + 1
        return self.edad

    def numeros_rojos(self, importe):
        return (self.saldo < 0 or (self.saldo - importe) < 0)

    def transferencia(self, persona2, importe):
        if not self.numeros_rojos(importe):
            self.saldo = self.saldo - importe
            persona2.saldo = persona2.saldo + importe
            return f"Transferencia de {importe} Realizada"
        else:
            return f"Transferencia de {importe} NO realizada, cuenta en NUMEROS ROJOS "


Persona1 = Persona("Pepe", 25, 100)
Persona2 = Persona("Ana", 35, 200)

importe = 10

print(Persona1)
print(Persona2)

print(Persona1.transferencia(Persona2, importe))

print(Persona1)
print(Persona2)
