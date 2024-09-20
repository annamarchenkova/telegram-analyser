import os
from openai import OpenAI
from dotenv import load_dotenv
from src.logger import logger

# Load credentials.env file if exists

load_dotenv(dotenv_path="config/.env")


class Config:
    """
    Configuration class to manage API keys and environment settings.
    Anthropic API keys are optional and used only if provided.
    """ 
    
    def __init__(self):
        """Initialize configuration class."""

        self.verbose = os.getenv("VERBOSE_MODE", True)

        # initialize credentials
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL_NAME")
        # self.client = OpenAI(api_key = self.openai_key)

        self.telegram_api_id = int(os.getenv("TELEGRAM_API_ID", 1))
        self.telegram_api_hash = os.getenv("TELEGRAM_API_HASH", "")
        self.telegram_phone = os.getenv("TELEGRAM_PHONE", "")
        self.telegram_chat_id = int(os.getenv("TELEGRAM_CHAT_ID", -4520808572))
        self.send_to_telegram = os.getenv("SEND_TO_TELEGRAM", False)
        self.save_to_file = os.getenv("SAVE_TO_FILE", True)

        # logger.info(f"Config initialized with: {self.__dict__}")
# Usage Example
config_obj = Config()