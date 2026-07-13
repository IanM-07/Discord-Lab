import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from memory import guardar_tema, obtener_historial, reiniciar_memoria
from reasoning import resolver

# ==========================
# Cargar variables de entorno
# ==========================

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# ==========================
# Configuración del bot
# ==========================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# ==========================
# Evento al iniciar el bot
# ==========================

@bot.event
async def on_ready():

    reiniciar_memoria()

    print(f"✅ Bot conectado como {bot.user}")

# ==========================
# Comando de prueba
# ==========================

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

    # ==========================
# Menú principal
# ==========================

@bot.command()
async def Hola(ctx):

    mensaje = (
        "🤖 **AGENTE TUTOR DE PROGRAMACIÓN ESTRUCTURADA**\n\n"
        "¡Hola! Soy un asistente diseñado para ayudarte a estudiar los temas de Programación Estructurada.\n\n"

        "📚 **¿Qué puedo hacer?**\n"
        "Puedo responder preguntas sobre las cinco unidades del curso.\n\n"

        "💬 **Ejemplos de preguntas:**\n"
        "• ¿Qué es un lenguaje de programación?\n"
        "• ¿Qué es un compilador?\n"
        "• ¿Qué es un IDE?\n"
        "• ¿Qué es una variable?\n"
        "• ¿Qué es un identificador?\n"
        "• ¿Qué es la estructura if?\n"
        "• ¿Qué es el ciclo while?\n"
        "• ¿Qué es una función?\n"
        "• ¿Qué es un arreglo?\n\n"

        "📖 **Comandos disponibles**\n"
        "• **!temas** → Muestra todos los temas disponibles.\n"
        "• **!historial** → Muestra las consultas realizadas durante esta sesión.\n"
        "• **!salir** → Finaliza el codigo y muestra mensaje de despedida.\n"
        "• **!ping** → Comprueba que el bot está funcionando."
    )

    await ctx.send(mensaje)

    # ==========================
# Temas disponibles
# ==========================

@bot.command()
async def temas(ctx):

    mensaje = (
        "📚 **TEMAS DISPONIBLES**\n\n"

        "🔹 **Unidad 1**\n"
        "• Lenguaje de programación\n"
        "• Importancia de los lenguajes\n"
        "• Alto nivel\n"
        "• Bajo nivel\n"
        "• Compilador\n"
        "• Intérprete\n"
        "• Compilación e interpretación\n\n"

        "🔹 **Unidad 2**\n"
        "• IDE\n"
        "• Estructura de un programa\n"
        "• Variables\n"
        "• Constantes\n"
        "• Identificadores\n"
        "• Palabras reservadas\n"
        "• Tipos de datos\n"
        "• Tipos de datos simples\n"
        "• Tipos de datos compuestos\n"
        "• Operadores\n"
        "• Operadores aritméticos\n"
        "• Operadores lógicos\n\n"

        "🔹 **Unidad 3**\n"
        "• Estructuras de control\n"
        "• Estructuras de selección\n"
        "• If\n"
        "• Then\n"
        "• If-Else\n"
        "• Switch\n"
        "• Estructuras de repetición\n"
        "• For\n"
        "• While\n"
        "• Do-While\n"
        "• Aplicación de algoritmos\n\n"

        "🔹 **Unidad 4**\n"
        "• Procedimientos\n"
        "• Funciones\n"
        "• Funciones de usuario\n"
        "• Funciones externas\n"
        "• Invocación\n"
        "• Parámetros\n"
        "• Parámetros de entrada\n"
        "• Parámetros de salida\n"
        "• Diferencias entre función y procedimiento\n"
        "• Bibliotecas\n\n"

        "🔹 **Unidad 5**\n"
        "• Arreglos\n"
        "• Vectores\n"
        "• Matrices\n"
        "• Declaración de arreglos\n"
        "• Lectura y escritura\n"
        "• Operaciones con arreglos"
    )

    await ctx.send(mensaje)

# ==========================
# Ver historial de consultas
# ==========================

@bot.command()
async def historial(ctx):

    historial = obtener_historial(str(ctx.author))

    if len(historial) == 0:
        await ctx.send("Todavía no has realizado consultas.")
        return

    respuesta = "**Historial de consultas**\n\n"

    for i, consulta in enumerate(historial, start=1):
        respuesta += (
            f"{i}. {consulta['pregunta']}\n"
            f"   Tema: {consulta['tema']}\n\n"
        )

    await ctx.send(respuesta)

# ==========================
# Escuchar mensajes
# ==========================

@bot.event
async def on_message(message):

    # Ignorar mensajes enviados por el propio bot
    if message.author.bot:
        return

    # Si es un comando, ejecutarlo y salir
    if message.content.startswith("!"):
        await bot.process_commands(message)
        return

    # Analizar la consulta
    respuesta, tema = resolver(message.content)

    # Si encontró un tema, guardarlo en la memoria
    if tema:
        guardar_tema(
            str(message.author),
            tema,
            message.content
        )

    # Enviar la respuesta
    if respuesta:
        await message.channel.send(respuesta)

# ==========================
# Iniciar el bot
# ==========================

    # ==========================
# Despedida
# ==========================

@bot.command()
async def salir(ctx):

    mensaje = (
        "👋 **Gracias por utilizar el Agente Tutor de Programación Estructurada.**\n\n"
        "Esperamos que este asistente te haya sido de ayuda para reforzar tus conocimientos.\n\n"
        "**Desarrollado por:**\n"
        "• Ian Morales\n"
        "• Alan Dominguez\n\n"
        "¡Hasta luego y mucho éxito en tus estudios!"
    )

    await ctx.send(mensaje)

bot.run(TOKEN)