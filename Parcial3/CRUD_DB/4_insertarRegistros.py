import conexionDB import *

try:
 micursor=conexionDB.conexion.cursor()
 sql="INSERT INTO clientes (id,nombre,direccion, tel) VALUES (NULL, 'juan Polainas', 'col. del valle', '618123456')"

 micursor.execute(sql)
 #Es necesario ejecutar el commit para que finalice el SQ con exito
 conexion.commit()

except:
 print("Ocurrio un error por favor vuelve a intentar... mas tarde ... :c")

else:
 print("Se inserto la informacion con exito")