import conexionDB import *

try:
 micursor=conexionDB.conexion.cursor()
 sql="UPDATE clientes set direccion 'col. del UTD' where id=1"

 micursor.execute(sql)
 #Es necesario ejecutar el commit para que finalice el SQ con exito
 conexion.commit()

except:
 print("Ocurrio un error por favor vuelve a intentar... mas tarde ... :c")

else:
 print("Registro Actualizado con exito")
