class ControlAcceso:
    def __init__(self):
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            return rol
        else:
            raise ValueError("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")

    def agregar_usuario(self, matricula, rol):
        self.usuarios_autorizados[matricula] = rol
        print(f"> Usuario {matricula} agregado con rol: {rol}.")

sistema = ControlAcceso()

print("--- Sistema de Seguridad Laboratorio IA - UX ---")

while True:
    try:
        matricula = input("\nIngrese su matrícula: ").strip()

        if not matricula:
            raise ValueError("Error: La matrícula no puede estar vacía.")

        rol = sistema.verificar_permisos(matricula)
        if rol == "Administrador":
            opcion = input("¿Desea agregar un nuevo usuario? (s/n): ").lower()
            if opcion == "s":
                nueva_matricula = input("Ingrese nueva matrícula: ").strip()
                nuevo_rol = input("Ingrese rol (Investigador/Estudiante): ").strip()
                sistema.agregar_usuario(nueva_matricula, nuevo_rol)

    except ValueError as e:
        print(e)

    finally:
        print("--- Intento de acceso registrado en el log del servidor ---")