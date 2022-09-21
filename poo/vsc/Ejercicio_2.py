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
        return  f"Nombre : {self.nombre} \n" +\
                f"Edad : {self.edad} \n" +\
                f"DNI : {self.DNI}"

    def esMayorDeEdad(self):
        return self.edad >= 18

# persona1 = Persona("Carlos", 1, "50000000A")
# persona2 = Persona("Maria", 18, "50000000A")

# print(persona1.mostrar())

# if persona2.esMayorDeEdad():
#     print(f"El cliente {persona2.nombre} es mayor de edad ")
# else:
#     print(f"El cliente {persona2.nombre} es menor de edad ")

# if persona1.esMayorDeEdad():
#     print(f"El cliente {persona1.nombre} es mayor de edad ")
# else:
#     print(f"El cliente {persona1.nombre} es menor de edad ")


# EJERCICIO 2
"""
    Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) 
    y cantidad (puede tener decimales).
    Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    mostrar(): Muestra los datos de la cuenta.
    ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
    no se hará nada.
    retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos 
    si es saldo negativo.
"""
class Cuenta(Persona):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar(self):
        if self.saldo >= 0:
            return  f"Titular : {self.titular} \n" +\
                    f"Saldo : {self.saldo} "
        else:
            return  f"Titular : {self.titular} \n" +\
                    f"Saldo : {self.saldo} \n" +\
                    f"CUENTA EN NUMEROS ROJOS"

    def ingresar(self, importe):
        if importe > 0:
            self.saldo  = self.saldo + importe

    def retirar(self, importe):
        if importe > 0:
            self.saldo  = self.saldo - importe
        return self.saldo

#cuenta1 = Cuenta("Carlos", 100)

#print(cuenta1.mostrar())


# 1) Ingresar en positivo

#cuenta1.ingresar(10)
#print(cuenta1.mostrar())

# 2) Ingresar negativo


#cuenta1.ingresar(-10)

#print(cuenta1.mostrar())


# 3) Retirar dinero

#cuenta1.retirar(20)

#print(cuenta1.mostrar())

# 4) Retirar dinero en número rojos

#cuenta1.retirar(100)

#print(cuenta1.mostrar())

# EJERCICIO 3

"""
    Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven 
    que deriva de la anterior.
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
class Cuenta_Joven(Cuenta):
    def __init__(self, titular, edad, saldo=0, bonificacion=0):
#        super().__init__(titular, saldo)
        self.titular = titular
        self.saldo = saldo

        self.bonificacion = bonificacion
        self.edad = edad

    def esTitularValido(self):
        return self.edad < 25 and self.esMayorDeEdad()
#        if self.esMayorDeEdad() and self.edad < 25:
#            esTitularValido = True
#            return esTitularValido
#        else:
#            esTitularValido = False
#            return esTitularValido

    def mostrar(self):
        return f"Cuenta Joven Titular {self.titular}, cantidad: {self.saldo}, edad {self.edad}  y bonificación {self.bonificacion} "

    # def retirar(self, cantidad):
    #     if not self.esTitularValido():
    #         print("No puedes retirar el importe")
    #     elif cantidad > 0:
    #         super().retirar(cantidad)

    def retirar_cuentajoven(self, importe):
        if not self.esTitularValido():
            print("No puedes retirar el importe")
        elif importe > 0:
            self.retirar(importe)
            print(f"Restirando efectivo {importe} ")


titular2 = Cuenta_Joven("Pedro", 30)
titular3 = Cuenta_Joven("Lorena", 20, 200, 5)
titular4 = Cuenta_Joven("Jaume", 24, 100, 5)


#print(titular3.mostrar())


# 1) Mayor de edad

#persona1 = Persona("Carlos", 19, "50000000A")
# if titular3.esMayorDeEdad:
#     print("Es mayor de edad")
# else:
#     print("NO Es mayor de edad")


# 2) Menor de edad
# titular4 = Cuenta_Joven("Lorena", 16, 200, 5)

# if titular4.esMayorDeEdad():
#     print("Es mayor de edad")
# else:
#     print("NO Es mayor de edad")

# Comprobar si el  cliente  es un titular válido para la Cuenta Joven

# if titular4.esTitularValido():
#    print("Es un titular válido")
# else:
#    print("NO ss un titular válido")

#operacion de ingresar y retirar en cuenta joven
print(titular4.mostrar())
titular4.retirar_cuentajoven(10)
print(titular4.mostrar())

titular4.ingresar(20)
print(titular4.mostrar())
