print("--- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---")

temperaturas = []
contador_errores = 0

for i in range(8):
    lectura = float(input(f"Lectura {i + 1}: "))
    temperaturas.append(lectura)

for i in range(8):
    if temperaturas[i] < 0 or temperaturas[i] > 100:
        temperaturas[i] = 35.0
        contador_errores += 1

print(f"\nSe detectaron {contador_errores} lecturas erróneas y fueron corregidas a 35.0.")

print("Datos limpios:", temperaturas)

suma = 0.0
for temp in temperaturas:
    suma += temp

promedio = suma / 8

print(f"Promedio de operación: {promedio:.2f}°C")

if promedio > 75:
    print("ALERTA: Activando sistema de enfriamiento líquido")
else:
    print("Estado: Operación normal")