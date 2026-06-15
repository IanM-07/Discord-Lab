from practica04.tareas_agente import agregar_tarea, listar_tareas, eliminar_tarea

def iniciar_agente():
    tareas = []
    prefijo = "!"

    print("=== Agente Procesador de Tareas ===")
    print("Comandos: !add [texto], !list, !del [numero], !exit")

    activo = True

    while activo:
        entrada = input(">> ").strip()

        if not entrada.startswith(prefijo):
            print("Recuerda usar '!' para comandos.")
            continue

        cuerpo = entrada[len(prefijo):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        if comando == "add":
            print(agregar_tarea(tareas, argumento))

        elif comando == "list":
            print(listar_tareas(tareas))

        elif comando == "del":
            print(eliminar_tarea(tareas, argumento))

        elif comando == "exit":
            print("Saliendo del agente...")
            activo = False

        else:
            print(f"Error: Comando '!{comando}' no reconocido.")


if __name__ == "__main__":
    iniciar_agente()