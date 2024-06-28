# una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular 
# como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutilizar
# con el simple hecho de invocarla es decir mandarla a llamar

#sintaxis

# def nombre de Min funcion(parametros):
# bloque o conjunto de i strucciones

# nombre de Mi funcion(parametros)

# Las funciones pueden ser de 4 tipos
# 1.- Funcion que no recibe parametros y no regresa valor
# 2.- Funcion que no recibe parametros y regresa Valor
# 3.- Funcion que recibe parametros y no regresa valor
# 4.- Funcion que recibe parametros y regresa valor


#1.- Funcion que no recibe parametros y no regresa valor 

# def sumaNumeros1():
#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2: "))
#     suma=n1+n2
#     print(f"{n1}+{n2}={suma}")

#     sumaNumeros1()

# 2.- Funcion que no recibe parametros y regresa Valor

# def sumaNumeros2():
#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2: "))
#     suma=n1+n2
#     return f"{n1}+{n2}={suma}"


# print(sumaNumeros2())

# 3.- Funcion que recibe parametros y no regresa valor

# def sumaNumeros3(n1,n2):
#     suma=n1+n2
#     print(f"{n1}+{n2}={suma}")


# n1=int(input("Numero #1: "))
# n2=int(input("Numero #2: "))

# sumaNumeros3(n1,n2)

# 4.- Funcion que recibe parametros y regresa valor

# def sumaNumeros4(n1,n2):
#     suma=n1+n2
#     return f"{n1}+{n2}={suma}"


# n1=int(input("Numero #1: "))
# n2=int(input("Numero #2: "))

# print(sumaNumeros4(n1,n2))

# Ejemplo 6.- crear un programa que solicite a traves de una funcion la siguiente
# informacion: Nombre del oaciente, edad,estatura, tipo de sangre y utilizar 
# los 4 tipos de funciones

#1

def datos1():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")
    
sumaNumeros1()