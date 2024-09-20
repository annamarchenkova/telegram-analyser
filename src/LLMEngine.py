from enum import Enum
from pydantic import BaseModel
from typing import Optional, Any

from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel
# from together import Together

from config.config_file import config_obj

#--------------------------------- Chat Model Engine --------------------------------#
class ChatModelName(Enum):
    OPENAI = "openai"
    # MISTRAL = "mistral"
    # TOGETHERAI = "togetherai"


class LLMSettings(BaseModel):
    model: str = "gpt-4o"
    temperature: int|float = 0
    top_p: Optional[Any] = None
    streaming: Optional[bool] = False
    max_tokens: Optional[int] = 4095
    callbacks: Optional[Any] = None
    
#--------------------------------- Get Chat Model Engine --------------------------------#
class LLMEngineAPI:
    def __init__(self,
                 engine_type: ChatModelName = ChatModelName.OPENAI,
                 **settings
                 ):
        
        self.engine_type = engine_type
        self.settings = LLMSettings(**settings)
    
    def get_chat_model(self) -> BaseChatModel:
        """Create and return a chat model instance based on the engine type and settings."""
        
        if self.engine_type == ChatModelName.OPENAI:
            return ChatOpenAI(
                openai_api_key=config_obj.openai_key,
                model_name=self.settings.model,
                temperature=self.settings.temperature,
                max_tokens=self.settings.max_tokens,
                streaming=self.settings.streaming,
                callbacks=self.settings.callbacks,
                model_kwargs={"top_p": self.settings.top_p,
                              } if self.settings.top_p is not None else {}
            )
        
        # elif self.engine_type == ChatModelName.MISTRAL:
        #     return ChatMistralAI(
        #         api_key=config_obj.mistral_key,
        #         model=self.settings.model,
        #         temperature=self.settings.temperature,
        #         max_tokens=self.settings.max_tokens,
        #         streaming=self.settings.streaming,
        #         callbacks=self.settings.callbacks
        #     )
        
        # elif self.engine_type == ChatModelName.TOGETHERAI:
        #     return ChatTogether(
        #         api_key=config_obj.together_key,
        #         model=self.settings.model,
        #         temperature=self.settings.temperature,
        #         max_tokens=self.settings.max_tokens,
        #         streaming=self.settings.streaming,
        #         callbacks=self.settings.callbacks
        #     )
        
        else:
            raise ValueError(f"Unsupported LLM type: {self.engine_type}")


#Usage
# mistral_engine = LLMEngineAPI(
#     engine_type=ChatModelName.MISTRAL,
#     model="open-mixtral-8x22b",
#     temperature=0.1,
#     max_tokens=10000,
# )

# llama_engine = LLMEngineAPI(
#     engine_type=ChatModelName.TOGETHERAI,
#     model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
#     temperature=0.0,
#     max_tokens=16000,
# )

gpt_engine = LLMEngineAPI(
    engine_type=ChatModelName.OPENAI,
)
