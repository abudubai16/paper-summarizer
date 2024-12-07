import os
import json
from typing import List

from src.utils import get_dirs
from src.const import MEMORY_BUFFER


from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.llms import ChatMessage
from llama_index.core.storage.chat_store import SimpleChatStore
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
        self.chat_store = SimpleChatStore.from_persist_path(self.chat_history_path)

    def save_chat_history(self, chat_history: List[ChatMessage]) -> None:
        """
            Save the chat history for the given paper to the chat store.
        """
        self.chat_store.set_messages(self.paper_name, chat_history)
        self.chat_store.persist(self.chat_history_path)

    def load_chat_history(self) -> ChatMemoryBuffer:
        """
            Load the chat history for the given paper from the chat store.
            If no history exists, return an empty list.
        """

        return ChatMemoryBuffer.from_defaults(self.chat_store.get_messages(self.paper_name))

    def add_message_to_chat_history(self, message: ChatMessage) -> None:
        """
            Add a single message to the chat history for the given paper.
        """
        self.chat_store.add_message(self.paper_name, message)
        self.chat_store.persist(self.chat_history_path)

    def delete_chat_history(self) -> None:
        """
            Delete the entire chat history for the given paper.
        """
        self.chat_store.delete_messages(self.paper_name)
        self.chat_store.persist(self.chat_history_path)