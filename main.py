from pyrogram import Client, filters
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("mi_sesion", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.private & filters.text)
async def recibir_dni(client, message):
    texto = message.text.strip()
    if texto.isdigit() and len(texto) == 8:
        await message.reply("🔎 Consultando DNI " + texto + "...")
        # Enviar comando al bot de LiderData
        lider_bot = await app.send_message("LiderDataBot", f"/dni{texto}")
        await lider_bot.forward(message.chat.id)
    else:
        await message.reply("❌ DNI inválido. Escribe un DNI de 8 dígitos.")

app.run()
