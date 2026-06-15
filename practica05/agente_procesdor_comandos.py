import datetime

from practica01.procesador_comandos import (
    obtener_saludo,
    procesar_comando_recordar,
    calcular_uptime,
    mostrar_ayuda
)

def iniciar_agente():
    Nombre_bot = "DISCORDIAN"
    prefijo = "!"
    hora_inicio = datetime.datetime.now()

    print(obtener_saludo(Nombre_bot))
    print("Escribe !ayuda para ver los comandos disponibles.")

    ejecutando = True

    while ejecutando:
        entrada = input(f"[{Nombre_bot}] Ingrese comando: ").strip()

        if not entrada.startswith(prefijo):
            print("Comando no reconocido")
            continue

        partes = entrada[len(prefijo):].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        if comando == "saludo":
            print(obtener_saludo(Nombre_bot))

        elif comando == "ayuda":
            print(mostrar_ayuda())

        elif comando == "recordar":
            print(procesar_comando_recordar(argumento))

        elif comando == "uptime":
            print(calcular_uptime(hora_inicio))

        elif comando == "salir":
            print("Hasta luego")
            ejecutando = False

        else:
            print("Comando no reconocido")


def main():
    iniciar_agente()


if __name__ == "__main__":
    main()