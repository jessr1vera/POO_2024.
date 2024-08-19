import tkinter as tk
from tkinter import ttk, messagebox
from conexionBD import crear_conexion

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Seguros")
        self.root.attributes('-fullscreen', True)  # Abrir en pantalla completa
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Aseguradora AXA", font=("Arial", 24)).pack(pady=20)

        ttk.Button(self.root, text="Clientes", command=self.open_client_window, width=35, padding=15).pack(pady=10)
        ttk.Button(self.root, text="Agentes", command=self.open_agent_window, width=35, padding=15).pack(pady=10)
        ttk.Button(self.root, text="Pagos", command=self.open_payment_window, width=35, padding=15).pack(pady=10)
        ttk.Button(self.root, text="Pólizas", command=self.open_policy_window, width=35, padding=15).pack(pady=10)
        ttk.Button(self.root, text="Siniestros", command=self.open_claim_window, width=35, padding=15).pack(pady=10)
        ttk.Button(self.root, text="Vehículos", command=self.open_vehicle_window, width=35, padding=15).pack(pady=10)
        ttk.Button(self.root, text="Salir", command=self.root.quit, width=35, padding=15).pack(pady=20)

    def open_client_window(self):
        ClientWindow(tk.Toplevel(self.root))

    def open_agent_window(self):
        AgentWindow(tk.Toplevel(self.root))

    def open_payment_window(self):
        PaymentWindow(tk.Toplevel(self.root))

    def open_policy_window(self):
        PolicyWindow(tk.Toplevel(self.root))

    def open_claim_window(self):
        ClaimWindow(tk.Toplevel(self.root))

    def open_vehicle_window(self):
        VehicleWindow(tk.Toplevel(self.root))

class CRUDWindow:
    def __init__(self, root, entity_name, fields, db_table, id_field):
        self.root = root
        self.entity_name = entity_name
        self.fields = fields
        self.db_table = db_table
        self.id_field = id_field
        self.root.title(f"Gestión de {entity_name}")
        self.root.attributes('-fullscreen', True)  # Pantalla completa
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill='both')

        ttk.Label(frame, text=f"Opciones de {self.entity_name}", font=("Arial", 24)).pack(pady=20)

        ttk.Button(frame, text=f"Agregar {self.entity_name}", command=lambda: self.open_form("Agregar"), width=35, padding=15).pack(pady=10)
        ttk.Button(frame, text=f"Actualizar {self.entity_name}", command=lambda: self.open_form("Actualizar"), width=35, padding=15).pack(pady=10)
        ttk.Button(frame, text=f"Eliminar {self.entity_name}", command=lambda: self.open_form("Eliminar"), width=35, padding=15).pack(pady=10)
        ttk.Button(frame, text=f"Consultar {self.entity_name}", command=lambda: self.open_form("Consultar"), width=35, padding=15).pack(pady=10)
        ttk.Button(frame, text="Regresar al Menú Principal", command=self.root.destroy, width=35, padding=15).pack(pady=20)
        ttk.Button(frame, text="Salir del Sistema", command=self.root.quit, width=35, padding=15).pack(pady=20)

    def open_form(self, action):
        form_window = tk.Toplevel(self.root)
        form_window.title(f"{action} {self.entity_name}")
        form_window.attributes('-fullscreen', True)  # Pantalla completa

        if action in ["Agregar", "Actualizar"]:
            entries = {}
            for field in self.fields:
                tk.Label(form_window, text=field, font=("Arial", 14)).pack(pady=5)
                entry = tk.Entry(form_window, font=("Arial", 14))
                entry.pack(pady=5, padx=10)
                entries[field] = entry

            if action == "Actualizar":
                tk.Label(form_window, text=f"ID del Registro a Actualizar ({self.id_field})", font=("Arial", 14)).pack(pady=5)
                id_entry = tk.Entry(form_window, font=("Arial", 14))
                id_entry.pack(pady=5, padx=10)
                entries[self.id_field] = id_entry

            tk.Button(form_window, text="Aceptar", command=lambda: self.submit_form(entries, action), font=("Arial", 14)).pack(pady=15)
        elif action == "Eliminar":
            tk.Label(form_window, text=f"ID del Registro a Eliminar ({self.id_field})", font=("Arial", 14)).pack(pady=5)
            id_entry = tk.Entry(form_window, font=("Arial", 14))
            id_entry.pack(pady=5, padx=10)
            tk.Button(form_window, text="Aceptar", command=lambda: self.submit_form({self.id_field: id_entry}, action), font=("Arial", 14)).pack(pady=15)
        elif action == "Consultar":
            tk.Button(form_window, text="Mostrar Registros", command=self.show_records, font=("Arial", 14)).pack(pady=15)

        tk.Button(form_window, text="Regresar al Menú Principal", command=form_window.destroy, font=("Arial", 14)).pack(pady=10)

    def submit_form(self, entries, action):
        data = {field: entry.get() for field, entry in entries.items() if field != self.id_field}
        id_value = entries.get(self.id_field, "").get() if self.id_field in entries else None
        
        print("Datos para la acción:", action)  # Agregado para depuración
        print("Datos:", data)
        print("ID:", id_value)

        try:
            conn = crear_conexion()
            cursor = conn.cursor()

            if action == "Agregar":
                # Verificar si el ID ya existe antes de insertar
                if self.id_field in data:
                    cursor.execute(f"SELECT COUNT(*) FROM {self.db_table} WHERE {self.id_field} = %s", (data.get(self.id_field),))
                    count = cursor.fetchone()[0]
                    if count > 0:
                        messagebox.showerror("Error", f"El {self.entity_name} con {self.id_field} ya existe.")
                        return

                columns = ", ".join(data.keys())
                placeholders = ", ".join(["%s"] * len(data))
                sql = f"INSERT INTO {self.db_table} ({columns}) VALUES ({placeholders})"
                cursor.execute(sql, tuple(data.values()))
                conn.commit()
                messagebox.showinfo("Información", f"{self.entity_name} agregado exitosamente.")
                
            elif action == "Actualizar":
                updates = ", ".join([f"{key} = %s" for key in data.keys()])
                sql = f"UPDATE {self.db_table} SET {updates} WHERE {self.id_field} = %s"
                cursor.execute(sql, tuple(data.values()) + (id_value,))
                conn.commit()
                messagebox.showinfo("Información", f"{self.entity_name} actualizado exitosamente.")
                
            elif action == "Eliminar":
                sql = f"DELETE FROM {self.db_table} WHERE {self.id_field} = %s"
                cursor.execute(sql, (id_value,))
                conn.commit()
                messagebox.showinfo("Información", f"{self.entity_name} eliminado exitosamente.")
                
            elif action == "Consultar":
                self.show_records()

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
        finally:
            conn.close()

    def show_records(self):
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            sql = f"SELECT * FROM {self.db_table}"
            cursor.execute(sql)
            results = cursor.fetchall()
            records = "\n".join([str(record) for record in results])
            messagebox.showinfo("Resultados", f"Registros de {self.entity_name}:\n{records}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
        finally:
            conn.close()

class ClientWindow(CRUDWindow):
    def __init__(self, root):
        super().__init__(root, "Clientes", ["idCliente", "nombre", "direccion", "telefono", "correo"], "clientes", "idCliente")

class AgentWindow(CRUDWindow):
    def __init__(self, root):
        super().__init__(root, "Agentes", ["idAgente", "nombre", "telefono", "correo"], "agentes", "idAgente")

class PaymentWindow(CRUDWindow):
    def __init__(self, root):
        super().__init__(root, "Pagos", ["idPago", "fechaPago", "monto", "metodoPago"], "pagos", "idPago")

class PolicyWindow(CRUDWindow):
    def __init__(self, root):
        super().__init__(root, "Pólizas", ["numeroPoliza", "fechaInicio", "fechaFin", "cobertura"], "polizas", "numeroPoliza")

class ClaimWindow(CRUDWindow):
    def __init__(self, root):
        super().__init__(root, "Siniestros", ["numeroSiniestro", "fecha", "descripcion" ], "siniestros", "numeroSiniestro")

class VehicleWindow(CRUDWindow):
    def __init__(self, root):
        super().__init__(root, "Vehículos", ["numeroPlaca", "marca", "modelo", "año"], "vehiculos", "numeroPlaca")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
