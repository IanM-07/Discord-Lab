import math
from datetime import date

def imprimir_encabezado():
    hoy = date.today()
    print("====================================")
    print("    SISTEMA DE SALUD INTELIGENTE    ")
    print("====================================")
    print(f"Fecha: {hoy}")
    print()


def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)


def evaluar_presion(presion_sistolica):
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

imprimir_encabezado()

try:
    nombre = input("Nombre del Paciente: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    presion = int(input("Presión Sistólica: "))

    imc = calcular_imc(peso, estatura)
    estado_presion = evaluar_presion(presion)
    print("\n--- RESULTADOS DEL ANÁLISIS ---")
    print(f"Paciente: {nombre}")
    print(f"IMC Calculado: {math.ceil(imc)}")
    print(f"Estado de Presión: {estado_presion}")
    print("-------------------------------")

except ValueError:
    print("\n[ERROR] Entrada inválida. Verifica que los datos sean numéricos.")