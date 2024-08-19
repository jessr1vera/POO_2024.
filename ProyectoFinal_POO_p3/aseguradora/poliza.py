from conexionBD import crear_conexion

class Poliza:
    def __init__(self, numeroPoliza, fechaInicio, fechaFin, cobertura, prima):
        self.numeroPoliza = numeroPoliza
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.cobertura = cobertura
        self.prima = prima

    def crear(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO polizas (numero_poliza, fecha_inicio, fecha_fin, cobertura, prima) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.numeroPoliza, self.fechaInicio, self.fechaFin, self.cobertura, self.prima))
        conexion.commit()
        conexion.close()

    @staticmethod
    def mostrar():
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM polizas")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    def actualizar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE polizas SET fecha_inicio = %s, fecha_fin = %s, cobertura = %s, prima = %s WHERE numero_poliza = %s"
        cursor.execute(sql, (self.fechaInicio, self.fechaFin, self.cobertura, self.prima, self.numeroPoliza))
        conexion.commit()
        conexion.close()

    def eliminar(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM polizas WHERE numero_poliza = %s"
        cursor.execute(sql, (self.numeroPoliza,))
        conexion.commit()
        conexion.close()
