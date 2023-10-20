class Persona:
    def __init__(self, nombre, identificacion, telefono, email, direccion):
        self.nombre = nombre
        self.identificacion = identificacion
        self._telefono = telefono  # Atributo privado
        self.email = email
        self.direccion = direccion

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.identificacion}, Teléfono: {self._telefono}, Email: {self.email}, Dirección: {self.direccion}"



class Cliente(Persona):
    def __init__(self, nombre, identificacion, telefono, email, direccion):
        super().__init__(nombre, identificacion, telefono, email, direccion)
        self.ultima_compra = ((), "")

    def compra(self, *productos):
        self.ultima_compra = (productos, "Fecha de la compra")

    def __str__(self):
        persona_info = super().__str__()
        cliente_info = f"Última Compra: {self.ultima_compra}"
        return f"{persona_info}, {cliente_info}"


class Empleado(Persona):
    numeroEmpleados = 0  # Atributo de clase para contar empleados

    def __init__(self, nombre, identificacion, telefono, email, direccion, numero_cuenta, seccion, supervisor):
        super().__init__(nombre, identificacion, telefono, email, direccion)
        self._numero_cuenta = numero_cuenta  # Atributo privado
        self.seccion = seccion
        self.supervisor = supervisor
        Empleado.numeroEmpleados += 1  # Incrementar el contador al crear un empleado

    def mostrar_numero_cuenta(self):
        return self._numero_cuenta

    def aumentar_numero_empleados(self):
        Empleado.numeroEmpleados += 1

    def reducir_numero_empleados(self):
        Empleado.numeroEmpleados -= 1

    def __str__(self):
        persona_info = super().__str__()
        empleado_info = f"Número de Cuenta: {self._numero_cuenta}, Sección: {self.seccion}, Supervisor: {self.supervisor}"
        return f"{persona_info}, {empleado_info}"

# Crear instancias de las clases
persona = Persona("Juan", 12345, "660123456", "juan@example.com", "lalala")
cliente = Cliente("Maria", 54321, "678060504", "maria@example.com", "lelelele")
cliente.compra("Patatas", "Fruta", "Pescado")
empleado = Empleado("Luis", 98765, "685848483", "luis@example.com", "lulululu", "12345678", "Ventas", "Elena")

# Mostrar información
print("Información de la Persona:")
print(persona)
print("\nInformación del Cliente:")
print(cliente)
print("\nInformación del Empleado:")
print(empleado)
print(f"Número de Empleados: {Empleado.numeroEmpleados}")
