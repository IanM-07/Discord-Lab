import json
import os

BASE = os.path.dirname(__file__)
ARCHIVO = os.path.join(BASE, "data", "usuarios.json")

# Crear la carpeta data si no existe
os.makedirs(os.path.join(BASE, "data"), exist_ok=True)


def guardar_tema(usuario, tema, pregunta):

    datos = {}

    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
            except:
                datos = {}

    if usuario not in datos:
        datos[usuario] = {
            "ultimo_tema": "",
            "historial": []
        }

    datos[usuario]["ultimo_tema"] = tema

    datos[usuario]["historial"].append({
        "pregunta": pregunta,
        "tema": tema
    })

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def obtener_historial(usuario):

    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)
        except:
            return []

    if usuario in datos:
        return datos[usuario]["historial"]

    return []


def reiniciar_memoria():

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump({}, archivo, indent=4)