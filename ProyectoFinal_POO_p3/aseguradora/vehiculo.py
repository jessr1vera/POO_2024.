from conexionBD import crear_conexion, cerrar_conexion

class Vehiculo:
    def __init__(self, numeroPlaca, marca, modelo, año):
        self.numeroPlaca = numeroPlaca
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def registrar_vehiculo(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO vehiculos (numeroPlaca, marca, modelo, año) VALUES (%s, %s, %s, %s)",
                (self.numeroPlaca, self.marca, self.modelo, self.año)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar vehículo: {e}")
            return False
        finally:
            cerrar_conexion(conexion)

    @staticmethod
    def mostrar_vehiculos():
        conexion = crear_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM vehiculos")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar vehículos: {e}")
            return []
        finally:
            cerrar_conexion(conexion)

    def actualizar_vehiculo(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "UPDATE vehiculos SET numeroPlaca=%s, marca=%s, modelo=%s, año=%s WHERE id=%s",
                (self.numeroPlaca, self.marca, self.modelo, self.año, self.id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar vehículo: {e}")
            return False
        finally:
            cerrar_conexion(conexion)

    @staticmethod
    def eliminar_vehiculo(id):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM vehiculos WHERE id=%s", (id,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar vehículo: {e}")
            return False
        finally:
            cerrar_conexion(conexion)

