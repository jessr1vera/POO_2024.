#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

numero1=input("ingrese el primer numero del 0 al 60 ")
numero2=input("ingrese el segundo numero del 0 al 60 ")

if int(numero1) and int(numero2)<=60:
    suma=int(numero1)+int(numero2)
    print(f"La suma es igual a:  {suma}")

    resta=int(numero1)-int(numero2)
    print(f"La resta es igual a:  {resta}")

    multi=int(numero1)*int(numero2)
    print(f"La multiplicacion es igual a:  {multi}")

    division=int(numero1)/int(numero2)
    print(f"La division es igual a:  {division}")

