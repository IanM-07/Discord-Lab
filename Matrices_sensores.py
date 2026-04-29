print("--- MÓDULO DE SENSORES (VECTORES) ---")

sensores_distancia = []

for i in range(5):
    while True:
        try:
            valor = float(input(f"Ingrese distancia sensor {i+1}: "))
            if valor < 0:
                print("Valor inválido. No puede ser negativo.")
                continue
            sensores_distancia.append(valor)
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

promedio = sum(sensores_distancia) / len(sensores_distancia)

if promedio < 2.0:
    print(f"\nPromedio de proximidad: {promedio}m. Aviso: Reduciendo velocidad global.")
else:
    print(f"\nPromedio de proximidad: {promedio}m. Estado: Seguro.")


print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")

camara_ia = []

print("\nLlenando matriz de cámara 3x3:")

for i in range(3):
    fila = []
    for j in range(3):
        while True:
            try:
                valor = int(input(f"Fila {i}, Col {j} (Brillo 0-255): "))
                
                # Saturación
                if valor > 255:
                    valor = 255
                if valor < 0:
                    valor = 0

                fila.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
    camara_ia.append(fila)


print("\nVisualización de la imagen capturada:\n")

for fila in camara_ia:
    print("[ ", end="")
    for valor in fila:
        print(f"{valor:3}", end=" ")
    print("]")


contador_brillo = 0

for fila in camara_ia:
    for valor in fila:
        if valor > 200:
            contador_brillo += 1

print("\nResultado de Análisis IA:")
print(f"Se detectaron {contador_brillo} píxeles de alta intensidad.")