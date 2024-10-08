# local imports
import os
from dotenv import load_dotenv  
load_dotenv('.venv')

# project imports
from src.const import DOWNLOAD_DIR, MEMORY_BUFFER, MODEL_NAME
from src.utils import file_metadata_extractor

# llama-index imports
import openai

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, PromptTemplate, StorageContext, load_index_from_storage
from llama_index.core.node_parser import SimpleNodeParser, SemanticSplitterNodeParser

from llama_index.core.chat_engine import CondensePlusContextChatEngine
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.memory import ChatMemoryBuffer

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

##############################################
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_index() -> VectorStoreIndex:
    assert len(os.listdir(DOWNLOAD_DIR)) != 0, 'There are no files in the downloads directory'

    reader = SimpleDirectoryReader(DOWNLOAD_DIR, file_metadata=file_metadata_extractor)
    document = reader.load_data(show_progress=True)

    print('Generating Index!')

    # parser = SimpleNodeParser.from_defaults(chunk_overlap=20, chunk_size=2048)
    parser = SemanticSplitterNodeParser(buffer_size=1, breakpoint_percentile_threshold=95, embed_model=OpenAIEmbedding(), )
    nodes = parser.get_nodes_from_documents(documents=document, show_progress=True) #32_000 words for the testing pdf
    index = VectorStoreIndex(nodes)
    
    print('Index Generated')

    return index

def load_temp_index() :
    storage_context = StorageContext.from_defaults(persist_dir=DOWNLOAD_DIR)
    index = load_index_from_storage(storage_context=storage_context)
    return index

def get_chat_engine(index_from_context=False) -> CondensePlusContextChatEngine:

    if index_from_context:
        index = load_temp_index()
    else:
        index = get_index()

    llm = OpenAI(model=MODEL_NAME)
    custom_prompt = PromptTemplate(
        """\
    Given a conversation (between Human and Assistant) and a follow up message from Human, \
    rewrite the message to be a standalone question that captures all relevant context \
    from the conversation.

    <Chat History>
    {chat_history}

    <Follow Up Message>
    {question}

    <Standalone question>
    """
    )
    custom_chat_history = [
        ChatMessage(
            role=MessageRole.USER,
            content="Hello assistant, we are having a insightful discussion about a research paper today.",
        ),
        ChatMessage(role=MessageRole.CHATBOT, content="Okay, sounds good."),
    ]
    chat_buffer = ChatMemoryBuffer.from_defaults(token_limit=MEMORY_BUFFER)

    chat_engine = CondensePlusContextChatEngine(
        llm=llm,
        memory=chat_buffer,
        retriever=index.as_retriever()
    )

    return chat_engine
    

def run_chat_engine(index_from_context=False) -> None:

    chat_engine = get_chat_engine(index_from_context)

    user_input = ''
    while user_input != 'bye':        
        print('>>>', end='')
        user_input = input()
        
        if user_input == 'bye':
            continue

        streaming_response = chat_engine.stream_chat(user_input) 
        for token in streaming_response.response_gen:
            print(token, end='')

        print('')
    pass

if __name__ == '__main__':
    index = get_index()
    print(type(index))    

    pass