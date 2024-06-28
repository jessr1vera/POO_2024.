# Ejemplo 1 (locales): realiza un programa que te pida ingresar la base y la altura 
# de un rectangulo, ademas de que imprima el resultado del area y perimetro

# def calcular_area_perimetro(base,altura):
    
#     area=0
#     perimetro=0

#     area=base * altura
#     perimetro=base*2 + altura*2
#     print(f"Un rectangulo con base {base} y altura {altura} tiene un area de: {area} y su perimetro es de: {perimetro}")

# base=int(input("Ingrese la base del rectangulo: "))
# altura=int(input("Ingrese la altura del rectangulo: "))
# calcular_area_perimetro(base,altura)


# Ejemplo 2 (globales): realiza un programa que calcule las tareas incompletas 
# que tienes que realizar utilizando las variables globales

tareas_completadas=0
tareas_incompletas=0
tareas=0

def mostrar_tareas_incompletas():
    print(f"¿Cuantas tareas tienes? ")
    print(f"Tienes un total de tareas: {tareas}, de las cuales realisaste: {tareas_completadas}, asi que tienes que hacer: {tareas_incompletas} ")

tareas=int(input("Ingrese la cantidad de tareas que tiene: "))
tareas_completadas=int(input("Ingrese la cantidad de tareas que ya realizo: "))

def completar_tareas():
    global tareas_completadas
    global tareas_incompletas
    tareas_incompletas= tareas - tareas_completadas

mostrar_tareas_incompletas()
completar_tareas()