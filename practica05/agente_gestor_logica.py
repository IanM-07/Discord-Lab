from practica03.agente_logica import (
    ejecutar_suma,
    buscar_en_diccionario,
    validar_variable,
    ejecutar_multiplicacion,
    obtener_fecha_completa
)

def iniciar_agente():
    prefijo = "!"

    print("=== Agente Gestor de Lógica ===")
    print("Comandos: !sumar, !multiplicar, !definir, !validar, !fecha, !salir")

    activo = True

    while activo:
        entrada = input(">> ").strip()

        if not entrada.startswith(prefijo):
            print("Usa '!' para comandos.")
            continue

        partes = entrada[len(prefijo):].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        if comando == "sumar":
            print(ejecutar_suma(argumento))

        elif comando == "multiplicar":
            print(ejecutar_multiplicacion(argumento))

        elif comando == "definir":
            print(buscar_en_diccionario(argumento))

        elif comando == "validar":
            print(validar_variable(argumento))

        elif comando == "fecha":
            print(obtener_fecha_completa())

        elif comando == "salir":
            print("Hasta luego.")
            activo = False

        else:
            print("Comando no reconocido.")

if __name__ == "__main__":
    iniciar_agente()