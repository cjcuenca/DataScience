# EJERCICIO 1
"""
    Crea una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    mostrar(): Muestra los datos de la persona.
    esMayorDeEdad(): Devuelve un valor indicando si es mayor de edad.
"""

class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def mostrar(self):
        return f"El usuario es {self.nombre}, de edad {self.edad}, con DNI {self.DNI}"

    def esMayorDeEdad(self):
        """El retorno será True o False"""
        return self.edad >= 18

persona1 = Persona("Juan García", 15, "71456789-T")
persona2 = Persona("María Pérez", 20, "14648794-S")

# Descomentar para ejecutar:
# print(persona1.mostrar())
# print(persona2.mostrar())

# print(persona1.esMayorDeEdad())
# print(persona2.esMayorDeEdad())

# EJERCICIO 2
"""
    Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
    Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    mostrar(): Muestra los datos de la cuenta.
    ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos si es saldo negativo.
"""

class Cuenta(Persona):

    def __init__(self, titularidad, cantidad=0.0):
        self.titularidad = titularidad
        self.cantidad = cantidad

    def mostrar(self):
        return f"Titular de la cuenta: {self.titularidad} con saldo {self.cantidad}"

    def ingresar(self, ingreso):
        if ingreso > 0:
            self.cantidad = self.cantidad + ingreso

    def retirar(self, retirada):
        # Retirada si es mayor que cero
        if retirada > 0:
            self.cantidad = self.cantidad - retirada
        # comprobación de saldo en cuenta
        if self.cantidad < 0:
            print(f"ATENCIÓN! La cuenta está en números rojos: {self.cantidad}")

titular1 = Cuenta("José Rodríguez")

# Descomentar para ejecutar:
# print(titular1.mostrar())

# 1) Ingresar en positivo

titular1.ingresar(20)


# Descomentar para ejecutar:
# print(titular1.mostrar())

# 2) Ingresar negativo

titular1.ingresar(-10)


# Descomentar para ejecutar:
# print(titular1.mostrar())

# 3) Retirar dinero

titular1.retirar(5)


# Descomentar para ejecutar:
# print(titular1.mostrar())

# 4) Retirar dinero en número rojos

titular1.retirar(20)


# Descomentar para ejecutar:
# print(titular1.mostrar())


# EJERCICIO 3

"""
    Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior.
    Cuando se crea esta nueva clase, además del titular y la cantidad se
    debe guardar una bonificación que estará expresada en tanto por ciento.
    Construye los siguientes métodos para la clase:

    Un constructor.
    En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad,
    por lo tanto hay que crear un método esTitularValido() que devuelve verdadero
    si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

    Además la retirada de dinero sólo se podrá hacer si el titular es válido.

    El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
    Piensa los métodos heredados de la clase madre que hay que reescribir.
"""
class CuentaJoven(Cuenta):

    def __init__(self,titularidad, edad, cantidad=0.0, bonificacion=0):
        super().__init__(titularidad, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    def mostrar(self):
        return f"-Cuenta Joven- Titular: {self.titularidad}, cantidad: {self.cantidad}, " +\
               f"Bonificacion: {self.bonificacion}, edad: {self.edad}"

    def esTitularValido(self):
        return self.edad < 25 and self.esMayorDeEdad()

    def retirar(self, cantidad):
        if not self.esTitularValido():
            print("No puedes retirar el dinero. Tirular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)

titular2 = CuentaJoven("Pedro Alonso", 30)
titular3 = CuentaJoven("Lorena García", 20, 200, 5)

# 1) Mayor de edad

# print(titular2.mostrar())

titular2.ingresar(100)

# print(titular2.mostrar())

titular2.retirar(100)

# print(titular2.mostrar())

# 2) Menor de edad

# print(titular3.mostrar())

titular3.ingresar(100)

# print(titular3.mostrar())

titular3.retirar(100)

# print(titular3.mostrar())