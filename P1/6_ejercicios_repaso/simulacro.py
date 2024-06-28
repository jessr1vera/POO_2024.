respuesta="si"
while respuesta == "si":
 articulo=(input("Ingrese un articulo "))
 
 precio=(input("Ingrese el precio unitario "))
 cantidad=(input("Ingrese la cantidad de articulos que desea "))

 iva=int(precio)*0.16 
 total_iva=iva*int(cantidad) 

 precio_iva=total_iva+int(precio)
 precio_total=precio_iva*int(cantidad)

 print(f"el precio total es:{precio_total}")

 respuesta=(input("¿Desea checar otro articulo? (si/no) "))