from conexionBD import crear_conexion, cerrar_conexion

class Pago:
    def __init__(self, idPago, fechaPago, monto, metodoPago):
        self.idPago = idPago
        self.fechaPago = fechaPago
        self.monto = monto
        self.metodoPago = metodoPago
       

    def registrar(self):
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO pagos (idPago, fechaPago, monto, metodoPago) VALUES (%s, %s, %s, %s)"
            values = (self.idPago, self.fechaPago, self.monto, self.metodoPago)
            try:
                cursor.execute(query, values)
                conexion.commit()
                return True
            except Exception as e:
                print(f"Error al registrar pago: {e}")
                return False
            finally:
                cerrar_conexion(conexion)

    @staticmethod
    def mostrar():
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            query = "SELECT * FROM pagos"
            try:
                cursor.execute(query)
                return cursor.fetchall()
            except Exception as e:
                print(f"Error al mostrar pagos: {e}")
                return []
            finally:
                cerrar_conexion(conexion)

    def actualizar(self):
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            query = "UPDATE pagos SET fechaPago=%s, monto=%s, metodoPago=%s  WHERE idPago=%s"
            values = (self.fechaPago, self.monto, self.metodoPago, self.idPago)
            try:
                cursor.execute(query, values)
                conexion.commit()
                return True
            except Exception as e:
                print(f"Error al actualizar pago: {e}")
                return False
            finally:
                cerrar_conexion(conexion)

    @staticmethod
    def eliminar(idPago):
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            query = "DELETE FROM pagos WHERE idPago=%s"
            try:
                cursor.execute(query, (idPago,))
                conexion.commit()
                return True
            except Exception as e:
                print(f"Error al eliminar pago: {e}")
                return False
            finally:
                cerrar_conexion(conexion)
