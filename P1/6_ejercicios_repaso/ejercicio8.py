# Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?


def calcular_porcentaje(porcentaje, numero):
    return (porcentaje / 100) * numero


porcentaje = float(input("Ingrese el porcentaje deseado: "))
numero = float(input("Ingrese el número: "))

resultado = calcular_porcentaje(porcentaje, numero)

print(f"El {porcentaje}% de {numero} es {resultado}")