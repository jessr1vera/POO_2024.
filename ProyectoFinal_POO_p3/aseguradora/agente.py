from conexionBD import crear_conexion

class Agente:
    def __init__(self, idAgente, nombre, telefono, correo):
        self.idAgente = idAgente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def registrar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO agentes (id_agente, nombre, telefono, correo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.idAgente, self.nombre, self.telefono, self.correo))
        conexion.commit()
        conexion.close()

    @staticmethod
    def mostrar():
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM agentes")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    def actualizar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE agentes SET nombre = %s, telefono = %s, correo = %s WHERE id_agente = %s"
        cursor.execute(sql, (self.nombre, self.telefono, self.correo, self.idAgente))
        conexion.commit()
        conexion.close()

    def eliminar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM agentes WHERE id_agente = %s"
        cursor.execute(sql, (self.idAgente,))
        conexion.commit()
        conexion.close()
