# main.py

import asyncio
from telegram_reader import TelegramReader
from message_analyzer import MessageAnalyzer

async def main():
    # Instantiate the TelegramReader
    reader = TelegramReader()

    # Connect to Telegram
    await reader.connect()

    # Specify the chat and date
    chat_id = 'CHAT_ID_OR_USERNAME'  # Replace with the chat ID or username
    target_date = '2024-09-19'  # Replace with the desired date (YYYY-MM-DD)

    # Download messages from the specified day
    messages = await reader.download_messages_from_day(chat_id, target_date)

    # Instantiate the MessageAnalyzer with the downloaded messages
    analyzer = MessageAnalyzer(messages)

    # Analyze the messages
    analysis_result = analyzer.analyze_messages()

    # (Optional) Summarize the messages
    summary_result = analyzer.summarize()

    # Disconnect from Telegram
    await reader.close()

if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
