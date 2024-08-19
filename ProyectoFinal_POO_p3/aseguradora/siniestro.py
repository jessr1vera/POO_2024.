from conexionBD import crear_conexion

class Siniestro:
    def __init__(self, numeroSiniestro, fecha, descripcion, montoReclamo):
        self.numeroSiniestro = numeroSiniestro
        self.fecha = fecha
        self.descripcion = descripcion
        self.montoReclamo = montoReclamo

    def reportar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO siniestros (numero_siniestro, fecha, descripcion, monto_reclamo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.numeroSiniestro, self.fecha, self.descripcion, self.montoReclamo))
        conexion.commit()
        conexion.close()

    @staticmethod
    def mostrar():
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM siniestros")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    def actualizar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE siniestros SET fecha = %s, descripcion = %s, monto_reclamo = %s WHERE numero_siniestro = %s"
        cursor.execute(sql, (self.fecha, self.descripcion, self.montoReclamo, self.numeroSiniestro))
        conexion.commit()
        conexion.close()

    def cerrar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM siniestros WHERE numero_siniestro = %s"
        cursor.execute(sql, (self.numeroSiniestro,))
        conexion.commit()
        conexion.close()
