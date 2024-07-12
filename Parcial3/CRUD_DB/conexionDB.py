import mysql.connector

#Conexion con la BD de MYSQL

try:
 conexion=mysql.connector.connect(
     host='localhost',
     user='root',
     password='',
     database='bd_python'
)

#verificar si la conexciion es correcta
except:
if conexion.is_connected():
    print("Se creo la conexion exitosamente c: ")
else:
    print("No fue posible conectar con la base de datos :c")

