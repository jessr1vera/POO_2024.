# Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

tabla_d = 1 
tabla_h = 10
desde = 1 
hasta = 10 

for num1 in range(tabla_d, tabla_h + 1):
	print(f"Tabla de multiplicar del {num1}:") 
	for num2 in range(desde, hasta + 1):
		print(f'{num1} x {num2} = {num1 * num2}')
	print() 