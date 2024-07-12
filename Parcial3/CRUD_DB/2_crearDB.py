import mysql.connector

try:
    # Conexión con la BD de Mysql
 conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='', 

 )

 #Crear un objeto nuevo de tipo cursor para ejecutar SQL
 micursor=conexion.cursor()
 sql="CREATE DATABASE bd_python"
 micursor.execute(sql)
 

except Exception as e:
   print(f"Error:{e}")
   print(f"Tipo De Error:{type(e).__name__}")
   print("Ocurrio un error, intentelo mas tarde ")
else:
  # Verificar si la conexion es correcta
    print(f"Se creo la bd exitosamente")
    micursor.execute("show databases")
    for x in micursor:
       print(x)