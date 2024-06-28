#manejo de erroes es la forma en la que tienen los lenguajes de porgramacion para evitar
# que sucedan errores en tiempo de ejecucion

#jemplo  1: Error cuando una variable no se genera

# try:
#     nombre=input("Dame el nombre: ")

#     if len(nombre)>1:
#      nombre_usuario="El nombre es: "+nombre

#     print(nombre_usuario)
# except:
#  print("Es necesario introducir un nombre de usuario...")

 
#  Ejemplo 2: cuando se solicita un numero y se introduce una letra
# ValueError: invalid literal for int() with base 10:tres

# try:
      
#  numero=int(input("Dame un numero: "))

#  if numero>0:
#      print("Soy un numero entero positivo c:")
#  else:
#      print("Soy un numero entero negativo :c")
# except:
#  print("No se puede convertir un dato no numerico a numero ")
# else:
#    print("Todo se ejecuto sin errores")

#Ejemplo 3: Cuando se generan multiples excepciones 

try:
 numero=int(input("Dame un numero: "))

 print("El cuadrado es: "+str(numero*numero))
except ValueError:
 print("Deebes introducir un numero, no se puede indtroducir un caracter que sea numerico")
except TypeError:
 print("No es posible convertir el numero a entero")
else:
 print("Finalizo correctamente c:")
finally:
 print("Listo, se termino :D")

