# List (Array)
# Son coleccioness o conjunto de datos/valores bajo
# un mismo nobre, para acceder a los valores se 
# hace con un indice numerico

# Nota: sus valores si son modificables

# La lista es una coleccion ordenada y modificable. Permite
# miembros duplicados.

# """"""

#crear una listaa con valores numericos, enteros e imprimir la lista



 #Ejemplo 2: crear una lista de palabras, posteriormente ingresar una palabra para buscar la coincidencia
 #en la lista e indicar si aparece la palabra y en que pocision, caso contratio
 #indicar una sola vez si no la encontro

# palabras=["hola","2024","10.23","True"]
# palabra_buscar = input("inserta palabra a buscar: ")

# if palabra_buscar in palabras:
#     for i, p in enumerate(palabras):
#         if p == palabra_buscar:
#             print(f"Encontré la palabra en la posición {i}")
# else:
#     print("No encontré la palabra en la lista")


# palabras=["hola","2024","10.23","True"]
# print(palabras)
# palabra_buscar = input("inserta palabra a buscar: ")

# noencontro=True
# while i<len(palabras):
#     if palabra_buscar==palabras[1]:
#      print(f"Encontre la palabra {palabra_buscar} en la pocision: {i}")
#      noencontro=False
    
#      i+=1


# # if noencontro:
#  print("No se encontro la palabra dentro de la lista")


#ejemplo 3 crea una lista multilinea o multidimensional (matriz) para crear una agenda telefonica

# agenda=[
#   ["Carlos", 618111223],
#   ["Fernando", 6187787787],
#   ["Matias", 618112222],
#   ["Juan Polainas",618777334 ],
# ]

# print(agenda)

# for i in agenda:
#   print(f"{agenda.index(i)+1 }.-{i}")

  #Ejemplo 4.- crear un programa que 
#   permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar,
# # remover, consultar peliculas
# #Notas
# #1.- Utilizar funciones
# 2.- Utilizar listas para alamacenar los nombres de las peliculas

def insertarPeliculas():
   pelicula=input("Ingrese l pelicula")
   peliculas.append(pelicula)
   espereTecla()

def eliminarPeliculas():
   pelicula=input("Ingrese l pelicula:  ")
   peliculas.remove (pelicula)
   espereTecla()

def consultarPeliculas():
   pelicula=input("Ingrese l pelicula:  ")
   print("Peliculas en la lista:")


 

peliculas=[]

print("\n\t..::: PELICULAS PIRATE :::... \n 1.- Agregar \n 2.- Eliminar \n 3.-Consultar \n 4.-Salir ")
opcion=input("\t Elige una opción: ").upper()

if opcion == '1':
    insertarPeliculas()
elif opcion == '2':
   eliminarPeliculas()
elif opcion == '3':
   consultarPeliculas()
elif opcion == '4':
 print("Saliendo del programa.")
else:
  print("Opción no válida, intente de nuevo.")