import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from telethon import TelegramClient
from config.config_file import config_obj

# Replace 'YOUR_API_ID', 'YOUR_API_HASH' with your actual API ID and hash.
api_id = config_obj.telegram_api_id
api_hash = config_obj.telegram_api_hash
chat_id = config_obj.telegram_chat_id
# Create a new client instance
client = TelegramClient('session_name', api_id, api_hash)

messages = [
    "123 находится в работе. Всё функционирует нормально.",
    "Временно простаивает 456, ожидаем запчасти.",
    "На техническом обслуживании 789. Плановое обслуживание до конца недели.",
    "987 требует ремонта. Обнаружены серьезные неисправности.",
    "Успешно завершила цикл переработки 654 и снова в работе.",
    "321 нуждается в замене. Возникли проблемы с мотором.",
    "Простаивает 852 из-за недостатка сырья.",
    "На ремонте 159. Необходима замена деталей.",
    "753 функционирует на полную мощность.",
    "Находится в эксплуатации 246, все системы работают исправно."
]

async def main():
    # Get the current user
    me = await client.get_me()
    # print(f'Logged in as: {me}')

    try:
        # Fetch all dialogs
        async for dialog in client.iter_dialogs():
            print(f"Chat: {dialog.name}, ID: {dialog.id}")
        
        for message in messages:
            try:
                # Send a message to the chat_id
                await client.send_message(chat_id, message)
                print(f"Message sent to {chat_id}")
            except Exception as e:
                print(f"Error: {e}")
        
    except Exception as e:
        print(f"Error: {e}")


# Run the main function
with client:
    client.loop.run_until_complete(main())
