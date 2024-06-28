# Crear un programa que solicite la calificacion de 15 alumnos 
# e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

num_alumnos = 15

calificaciones = []


for i in range(num_alumnos):
    calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
    calificaciones.append(calificacion)


aprobados = 0
no_aprobados = 0
si_aprobados = 60  

for calificacion in calificaciones:
    if calificacion >= si_aprobados:
        aprobados += 1
    else:
        no_aprobados += 1


print(f"Cantidad de alumnos aprobados: {aprobados}")
print(f"Cantidad de alumnos no aprobados: {no_aprobados}")