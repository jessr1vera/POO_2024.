# Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))



if a > b:
    print("El primer número debe ser menor o igual al segundo.")
else:
    for numero in range(a, b + 1):
        if numero % 2 != 0:
         print(numero)