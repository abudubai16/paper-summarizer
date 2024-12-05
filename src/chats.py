import os
import json

from src.utils import get_dirs
from src.const import MEMORY_BUFFER


from llama_index.core.memory import ChatMemoryBuffer
#################################################################

class ChatManager:
    """
        Manages saving, loading, and deleting chat history for a specific paper.
    """

    def __init__(self, paper_name: str, memory_buffer: int = MEMORY_BUFFER):
        self.paper_name = paper_name
        self.memory_buffer = memory_buffer
        self.dirs = get_dirs(self.paper_name)
        self.chat_history_path = os.path.join(self.dirs['chats'], 'chat_history.json')


    def save_chat_history(self, chat_buffer: ChatMemoryBuffer) -> None:
        """
            Save the chat history to a JSON file.
        """
        with open(self.chat_history_path, 'w') as file:
            json.dump(chat_buffer.to_dict(), file)


    def load_chat_history(self) -> ChatMemoryBuffer:
        """
            Load the chat history from a file, if the file doesn't exist or is corrupted, return an empty chat buffer.
        """
        try:
            with open(self.chat_history_path, 'r') as file:
                chat_data = json.load(file)
            print(f"Chat history loaded from {self.chat_history_path}")
            return ChatMemoryBuffer.from_dict(chat_data)
        except FileNotFoundError:
            print(f"No chat history found at {self.chat_history_path}. Starting fresh.")
            return ChatMemoryBuffer.from_defaults(token_limit=self.memory_buffer)
        except Exception as e:
            print(f"Error loading chat history: {e}")
            print("Starting with an empty chat buffer.")
            return ChatMemoryBuffer.from_defaults(token_limit=self.memory_buffer)

    def delete_chat_history(self) -> None:
        """
            Delete the chat history file.
        """
        try:
            os.remove(self.chat_history_path)
            print(f"Chat history file {self.chat_history_path} deleted.")
        except FileNotFoundError:
            print(f"No chat history file found at {self.chat_history_path} to delete.")
        except Exception as e:
            print(f"Error deleting chat history: {e}")