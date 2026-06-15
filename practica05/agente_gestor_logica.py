from agente_logica import analizar_comando

if __name__ == "__main__":
    print("--- Gestor del Agente en Discord ---")
    print("Escribe !ayuda para ver los comandos.")
    
    while True:
        entrada = input("Alumno >> ")
        
        if entrada.lower() in ["salir", "exit"]:
            break
        
        respuesta = analizar_comando(entrada)
        print(f"Bot >> {respuesta}\n")