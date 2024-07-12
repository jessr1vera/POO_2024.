import conexionDB import *

try:
 micursor=conexionDB.conexion.cursor()
 sql="delete from clientes where direccion='valle'"

 micursor.execute(sql)
 #Es necesario ejecutar el commit para que finalice el SQ con exito
 conexion.commit()

except:
 print("Ocurrio un error por favor vuelve a intentar... mas tarde ... :c")

else:
 print("Registro eliminado con exito")


 