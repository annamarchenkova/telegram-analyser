# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import asyncio
from telegram_reader import TelegramReader
from message_analyser import MessageAnalyzer
from config.config_file import config_obj
from logger import logger

async def main():
    # Instantiate the TelegramReader
    reader = TelegramReader()

    target_date = '2024-09-19'  # Replace with the desired date (YYYY-MM-DD)

    # Download messages from the specified day
    messages = await reader.get_messages_from_day(target_date)
    logger.info(f"Messages downloaded: {messages}")
    # Instantiate the MessageAnalyzer with the downloaded messages
    analyzer = MessageAnalyzer(messages, config_obj.openai_key, config_obj.openai_model)

    user_prompt = """Below there are messages about the status of different plastic recycling machines in Russian. Analyze these messages and return statistics about the status of the machines in the following format: 
        Total number of machines: <total_number_of_machines>
        #########################################################
        Total number of machines in operation: <total_number_of_machines_in_operation>
        Ids of machines in operation: <list_of_ids_of_machines_in_operation>
        Total number of machines in idle: <total_number_of_machines_in_idle>
        Ids of machines in idle: <list_of_ids_of_machines_in_idle>
        Total number of machines in maintenance: <total_number_of_machines_in_maintenance>
        Ids of machines in maintenance: <list_of_ids_of_machines_in_maintenance>
        Total number of machines in need of repair: <total_number_of_machines_in_need_of_repair>
        Ids of machines in need of repair: <list_of_ids_of_machines_in_need_of_repair>
        Total number of machines in need of replacement: <total_number_of_machines_in_need_of_replacement>
        Ids of machines in need of replacement: <list_of_ids_of_machines_in_need_of_replacement>

        Use only the information in the messages. Do not invent information."""
    
    # Analyze the messages
    analysis_result = analyzer.analyze_messages(user_prompt)
    logger.info(f"Analysis results: ", analysis_result=analysis_result)

    # if config_obj.send_to_telegram:
    #     # Send the analysis result to the Telegram chat
    #     await reader.send_message(analysis_result)
    #     logger.info(f"Analysis results sent to Telegram: {analysis_result}")

    if config_obj.save_to_file:
        # Save the analysis result to a file
        with open(f'output/results_{target_date}.txt', 'w') as file:
            file.write(analysis_result)

        logger.info(f"Analysis results saved to file: output/results_{target_date}.txt")

    # Add this line to exit the program
    sys.exit()

if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
