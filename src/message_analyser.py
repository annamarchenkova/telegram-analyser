import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

from pydantic import BaseModel, Field
from typing import List
from openai import OpenAI
from langchain_core.messages import HumanMessage
from LLMEngine import gpt_engine
from config.config_file import config_obj
from src.logger import logger

gpt = gpt_engine.get_chat_model()

class TelegramMessage(BaseModel):
    content: str
    sender: str = Field(..., min_length=1)
    timestamp: str

class MessageAnalyzer:
    def __init__(self, messages, openai_key, openai_model):
        self.messages = messages
        self.openai_key = openai_key
        self.openai_model = openai_model

    def analyze_messages(self, user_prompt: str) -> str:
        """
        Analyzes messages using OpenAI based on a user prompt.
        
        Args:
            user_prompt (str): The prompt to guide the analysis.
        
        Returns:
            dict: The analysis result from OpenAI.
        """
        logger.info(f"N messages to analyse:", n_messages=len(self.messages))
        if len(user_prompt) < 10:
            logger.info("User prompt is too short, using default prompt: 'Analyze these messages:'")

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

        client = OpenAI(api_key=self.openai_key)
        prompt = f"{user_prompt}\n{self.messages}"
        # logger.info(f"Prompt: {prompt}")
        messages = [HumanMessage(content=prompt)]
        
        try:
            response = gpt.invoke(messages)
            response_content = str(response.content)
        except Exception as e:
            logger.error(f"Error analyzing messages: {e}")
            return "Error analyzing messages"

        if config_obj.verbose:
            logger.info(f"AI response: ", ai_response=response_content)
        
        return response_content


