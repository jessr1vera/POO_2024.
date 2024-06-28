# print("...:::CALCULADORA BASICA:::...¨\n1- suma\n2- resta\n3- multiplicacion\n4- Division\n5- Salir")

# opcion=input("Elija la operacion que desea realizar: ").upper()

# if opcion =="5" or opcion=="SALIR":
#  print("Gracias por usar mi sistema, BYE c: ")


# else:
#  n1=int(input("Numero #1: "))
#  n2=int(input("Numero #2: "))



# if opcion=="1"  or opcion=="+" or opcion=="SUMA":
#  print(f"{n1}+{n2}={n1+n2}")

# elif opcion=="2"  or opcion=="-" or opcion=="RESTA":
#  print(f"{n1}-{n2}={n1-n2}")

# elif opcion=="3"  or opcion=="*" or opcion=="MULTIPLICACION":
#  print(f"{n1}*{n2}={n1*n2}")

# elif opcion=="4"  or opcion=="/" or opcion=="DIVISION":
#  print(f"{n1}/{n2}={n1/n1}")

#  def solicitarNumeros():
#   global n1,n2n1=int(input("Numero #1"))

def solicitarNumeros():
    global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}*{n2}={n1/n2}"
    else:
        opcion=False
        return "Gracias por utilizar el sistema ..."
        def espereTecla():
         print ("Oprima cualquier tecla para continuar...")
         input()
            

import os

opcion=True
while opcion:
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    solicitarNumeros()
    print(calculadora(n1,n2,opcion))
    