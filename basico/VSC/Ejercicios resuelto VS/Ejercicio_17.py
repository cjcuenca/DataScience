# EJERCICIO 1

"""
    Crea la clase "matematicas" y dentro de esa clase crea las funciones suma y resta,
    en dichas funciones nos deberán devolver el resultado de la suma y de la resta, siguiendo los siguientes pasos:
"""

# Crea la clase matematicas
# crea la funcion suma en la cual se le pase un valor (x):
#           y = 10 + x
#           retornar el resultado
# crea la funcion resta en la cual se le pase un valor(x):
#           y = 10- x
#           retornar el resultado
# Imprime el resultado de la función suma y de la funcion resta para un valor de x = 5, x = 10

class Matematicas:
    def suma(x):
        return 10 + x

    def resta(x):
        return 10 - x

    # Descomentar para ejecutar:
    # print("Estamos dentro de la clase matemáticas:")
    # print("Suma 5: ", suma(5))
    # print("Resta 5: ", resta(5))

# Descomentar para ejecutar:

# Para un valor de x es 5:
# print("### Estamos fuera de la clase matematicas:")
# print("Suma 5: ", Matematicas.suma(5))
# print("Resta 5: ", Matematicas.resta(5))

# Para un valor de x es 10
# print("Suma 5: ", Matematicas.suma(10))
# print("Resta 5: ", Matematicas.resta(10))


# EJERCICIO 2

"""
    Crea dos clases una llamala "libros" y otra clase "materias".

    A la clase libros declara una función con nombre "tipos" y dentro de clase materias declara una función con nombre "asignaturas".

    A la función tipos retorne el valor name = "Data Science" y la función asignaturas retorne nombre = "Big Data"
"""

class Libros:
    def tipos():
        return "Data Science"

# class Materias:
#     def asignaturas():
#         return "Big Data"

class Materias(Libros):
    def asignaturas():
        return "Big Data"

# 1) Prueba a retornar el resultados de la clase libros y la función tipos

# Descomentar para ejecutar:
# print("Resultado de clase libros, funcion tipos: ", Libros.tipos())

# 2) Prueba a retornar el resultados de la clase materias y la función asignaturas

# Descomentar para ejecutar:
# print("Resultado de clase Materias, funcion asignaturas: ", Materias.asignaturas())

# 3) Prueba a retornar el resultados de la clase materias y la función tipos
    # ¿ Qué es lo que observas ?

# print("Resultado de clase Materias, funcion tipos: ", Materias.tipos())

# Nos muestra un error de AttributeError: type object 'Materias' has no attribute 'tipos'
# Para corregirlo deberá heredar la función tipo de la clase Libros:

# Descomentar para ejecutar:
# print("Resultado de clase Materias, funcion tipos: ", Materias.tipos())