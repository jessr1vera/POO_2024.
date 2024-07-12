import conexionDB import *

try:
 micursor=conexionDB.conexion.cursor()
 sql="select * from clientes"
 micursor.execute(sql)

 resultado=micursor.fetchall()

 for fila in resultado:
     print(f"id:{fila[0]} - Nombre:{fila[1]} - Direccion: {fila[2]} - Tel: {fila[3]}")

except:
 print("Ocurrio un error por favor vuelve a intentar... mas tarde ... :c")

else:
 print("Registros consultados con exito")

 