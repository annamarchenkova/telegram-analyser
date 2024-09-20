import sys
import os
from datetime import datetime, timedelta
from telethon import TelegramClient
from config.config_file import config_obj

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

class TelegramReader:
    def __init__(self):
        self.api_id = config_obj.telegram_api_id
        self.api_hash = config_obj.telegram_api_hash
        self.chat_id = config_obj.telegram_chat_id
        self.client = TelegramClient('session_name', self.api_id, self.api_hash)

    async def get_messages_from_day(self, target_date=None, save_to_file=True):
        if target_date is None:
            target_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        
        target_date = datetime.strptime(target_date, "%Y-%m-%d").replace(tzinfo=datetime.now().astimezone().tzinfo)
        next_day = target_date + timedelta(days=1)
        
        async with self.client:
            messages = []
            async for message in self.client.iter_messages(self.chat_id, offset_date=next_day, reverse=True):
                if message.date == target_date:
                    break
                messages.append(message)

            if save_to_file:
                self._save_messages_to_file(messages, target_date)

            messages_list = [f"{msg.date}: {msg.sender_id}: {msg.text}" for msg in messages]

        return messages_list

    def _save_messages_to_file(self, messages, target_date):
        with open(f'messages_{target_date.strftime("%Y_%m_%d")}.txt', 'w', encoding='utf-8') as f:
            for msg in messages:
                f.write(f"{msg.date}: {msg.sender_id}: {msg.text}\n")

    async def send_message(self, message: str):
        await self.client.send_message(self.chat_id, message)

    async def run(self):
        await self.get_messages_from_day()

if __name__ == "__main__":
    reader = TelegramReader()
    with reader.client:
        reader.client.loop.run_until_complete(reader.run())
