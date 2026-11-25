import os
import discord
from google import genai

# =========================
# CONFIGURACIÓN
# =========================

TOKEN = os.getenv("TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Cliente de Gemini
cliente_ia = genai.Client(api_key=GEMINI_API_KEY)

# Discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# =========================
# EVENTOS
# =========================

@client.event
async def on_ready():
    print(f"✅ Conectado como {client.user}")

@client.event
async def on_message(message):

    # Ignorar mensajes de bots
    if message.author.bot:
        return

    # Comando de prueba
    if message.content.lower() == "!hola":
        await message.channel.send("Hola Enmanuel 😎")
        return

    # Comando IA
    if message.content.startswith("!ia "):

        pregunta = message.content[4:].strip()

        if not pregunta:
            await message.channel.send("Escribe una pregunta después de !ia")
            return

        try:

            respuesta = cliente_ia.models.generate_content(
                model="gemini-3.5-flash",
                contents=pregunta
            )

            texto = respuesta.text

            if len(texto) > 1900:
                texto = texto[:1900]

            await message.channel.send(texto)

        except Exception as e:

            print("ERROR GEMINI:")
            print(e)

            await message.channel.send(
                "⚠️ La IA no pudo responder. Inténtalo de nuevo en unos segundos."
            )

# =========================
# INICIAR BOT
# =========================

client.run(TOKEN)
