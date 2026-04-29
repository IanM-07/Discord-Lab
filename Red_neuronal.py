class MonitorEntrenamiento:
    def __init__(self, umbral_convergencia=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral_convergencia

    def registrar_epoca(self, valor_error):
        if valor_error < self.umbral_convergencia:
            print("[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")
        
        self.historial_errores.append(valor_error)
        print("> Registro exitoso.")


print("--- Iniciando Monitor de Red Neuronal ---")

monitor = MonitorEntrenamiento()

epocas_registradas = 0

while epocas_registradas < 5:
    try:
        entrada = input(f"\nIngrese el error de la Época {epocas_registradas + 1}: ")
        valor = float(entrada)

        if valor < 0:
            raise ValueError("No se permiten valores negativos.")

        monitor.registrar_epoca(valor)
        epocas_registradas += 1

    except ValueError:
        print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal válido y positivo.")


print("\n--- Resumen de Entrenamiento ---")

if len(monitor.historial_errores) > 0:
    historial = monitor.historial_errores
    promedio = sum(historial) / len(historial)
    mejor_error = min(historial)

    print(f"Historial: {historial}")
    print(f"Promedio de Error: {promedio}")
    print(f"Mejor resultado obtenido: {mejor_error}")
else:
    print("No se registraron datos.")