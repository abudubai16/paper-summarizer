import os


# Dictories
WORKING_DIR=os.getcwd()
DOWNLOAD_DIR=os.path.join(WORKING_DIR, 'downloads')
PROMPTS_DIR=os.path.join(WORKING_DIR, 'prompts')
DEFAULT_PROMPT_LOC=os.path.join(PROMPTS_DIR, "starting_prompts.txt")
INDEXES_DIR=os.path.join(WORKING_DIR, 'indexes')

# System capabilities
SYSTEM_CAPABILITIES=None


# OpenAI API
MEMORY_BUFFER=4096
MODEL_NAME='gpt-3.5-turbo'
USE_OPENAI_MODELS=False