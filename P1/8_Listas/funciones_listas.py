paises=["Mexico","USA","Brasil","china"]
numeros=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]

#Ordenar las listas
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#Agregar elementos a la lista
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)

#Remover elementos
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros)

#dar la vuelta a los segmentos de una lista

print(varios)
varios.reverse()
print(varios)
      
#buscar un valor dentro de una lista

encontro="Brasil" in paises
print(encontro)

#vaciar una lista
print(paises)
paises.clear()
print(paises)

#Unir listas
print(varios)
varios.extend(numeros)
print(varios)
