from conexionBD import crear_conexion

class Cliente:
    def __init__(self, idCliente, nombre, telefono, correo):
        self.idCliente = idCliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def registrar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO clientes (id_cliente, nombre, telefono, correo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.idCliente, self.nombre, self.telefono, self.correo))
        conexion.commit()
        conexion.close()

    @staticmethod
    def mostrar():
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    def actualizar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE clientes SET nombre = %s, telefono = %s, correo = %s WHERE id_cliente = %s"
        cursor.execute(sql, (self.nombre, self.telefono, self.correo, self.idCliente))
        conexion.commit()
        conexion.close()

    def eliminar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM clientes WHERE id_cliente = %s"
        cursor.execute(sql, (self.idCliente,))
        conexion.commit()
        conexion.close()

    @classmethod
    def get_fields(cls):
        return ["id_cliente", "nombre", "direccion", "telefono", "email"]
    
