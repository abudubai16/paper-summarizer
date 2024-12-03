import os


# Dictories
WORKING_DIR = os.getcwd()
DOWNLOAD_DIR = os.path.join(WORKING_DIR, 'downloads')

# System capabilities
SYSTEM_CAPABILITIES=None

# OpenAI API
MEMORY_BUFFER = 4096
MODEL_NAME = 'gpt-3.5-turbo'
USE_OPENAI_MODELS = False