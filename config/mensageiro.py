import os 
import telegram
import requests

async def enviar_mensagem(text):
    chat_id = os.getenv('id_chat')
    mensagem = text

    bot_token = os.getenv('token_bot')
    bot = telegram.Bot(token=bot_token)

    await bot.send_message(chat_id=chat_id, text=mensagem)
