# telegram_reader.py

from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class TelegramReader:
    def __init__(self):
        # Initialize the client using credentials from environment variables
        self.api_id = os.getenv('API_ID')
        self.api_hash = os.getenv('API_HASH')
        self.phone = os.getenv('PHONE')
        self.client = TelegramClient('session_name', self.api_id, self.api_hash)
    
    async def connect(self):
        # Connect to the Telegram API
        await self.client.start(self.phone)
    
    async def download_messages_from_day(self, chat_id, target_date):
        # Convert the date to a datetime object
        target_date = datetime.strptime(target_date, "%Y-%m-%d")
        next_day = target_date + timedelta(days=1)
        
        # Fetch messages from the chat within the specific day range
        messages = []
        async for message in self.client.iter_messages(chat_id, offset_date=next_day, reverse=True):
            if message.date < target_date:
                break
            messages.append(message)
        
        # Save messages to a file
        file_name = f'messages_{target_date.strftime("%Y_%m_%d")}.txt'
        with open(file_name, 'w', encoding='utf-8') as f:
            for msg in messages:
                f.write(f"{msg.date}: {msg.sender_id}: {msg.text}\n")
        
        print(f"Messages saved to {file_name}")

    async def close(self):
        # Disconnect the client
        await self.client.disconnect()
