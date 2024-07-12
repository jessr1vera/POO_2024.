import conexionDB 

try:
    micursor = conexionDB.conexion.cursor()
    sql = """CREATE TABLE clientes (
                id INT PRIMARY KEY AUTO_INCREMENT, 
                nombre VARCHAR(60), 
                direccion VARCHAR(120), 
                tel VARCHAR(10)
             )"""

    micursor.execute(sql)

except:
 print("Ocurrio un error por favor vuelve a intentar... mas tarde ... :c")

else:
 print("Se creo la tabla con exito")
 
