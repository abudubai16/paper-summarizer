import os
from click import prompt
from dotenv import load_dotenv
from sympy import N
load_dotenv('.venv')

from src.const import MODEL_NAME, MEMORY_BUFFER
from src.utils import load_prompts
from src.chats import ChatManager
from src.indexes import IndexManager

import openai

from llama_index.llms.openai import OpenAI
from llama_index.core.chat_engine import CondensePlusContextChatEngine
###################################################################
"""
    Structure of indexes and chats:
    indexes{
        index_name: {
            index: indexes for the RAG
            chats: chat history
        }
    }
"""


openai.api_key = os.getenv("OPENAI_API_KEY")

#TODO: Check the arguments to the chat engine, and check the creation of the prompts as well
class ChatEngineOpenAI:
    def __init__(self, index_manager: IndexManager, chat_manager: ChatManager, prompt, memory_buffer=MEMORY_BUFFER):
        """
        Initializes the chat engine.
        
        Args:
            index_manager (IndexManager): Manages the RAG index.
            chat_manager (ChatManager): Manages the chat history.
            prompt (PromptTemplate): Initial context prompt for the chat engine.
            memory_buffer (int): Token limit for chat memory buffer.
        """
        self.llm = OpenAI(model=MODEL_NAME)
        self.index_manager = index_manager
        self.chat_manager = chat_manager
        self.prompt = prompt

        self.chat_engine = self._create_chat_engine()

    def _create_chat_engine(self):
        """
            Create and initialize the chat engine.
        """
        retriever = self.index_manager.load_index().as_retriever()
        chat_buffer = self.chat_manager.load_chat_history()

        chat_engine = CondensePlusContextChatEngine(
            llm=self.llm,
            memory=chat_buffer,
            retriever=retriever,
            context_prompt=self.prompt
        )
        print("Chat engine initialized.")
        return chat_engine

    def run(self):
        """
            Run the chat engine in an interactive loop.
        """
        user_input = ''

        while user_input.lower() != 'bye':
            print('>>>', end=' ')
            user_input = input()
            if user_input.lower() == 'bye':
                print("Exiting chat.")

                self.chat_manager.save_chat_history(self.chat_engine.chat_history)
                break

            streaming_response = self.chat_engine.stream_chat(user_input)
            for token in streaming_response.response_gen:
                print(token, end='')

            print('')


def run_engine():
    
    pass 