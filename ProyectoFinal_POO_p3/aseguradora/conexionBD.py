import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='aseguradora',
            port=3307
        )
        if conexion.is_connected():
            #print("Conexión exitosa a la base de datos.")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        #print("Conexión cerrada.")
