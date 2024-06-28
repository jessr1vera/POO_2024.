# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

#usando while
respuesta="si"
while respuesta == "si":
 print("escriba un nuemro del 0 al 59: ")
 numero = int(input(""))

 cuadrado = numero**2

 print("El cuadrado de este numero es: ")
 print(cuadrado)
 respuesta=input("¿Desea checar otro numero?")

 #usando for