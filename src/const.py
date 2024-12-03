import os

from src.utils import get_file_path

WORKING_DIR = get_file_path()
DOWNLOAD_DIR = os.path.join(WORKING_DIR, 'downloads')

MEMORY_BUFFER = 4096
MODEL_NAME = 'gpt-3.5-turbo'
USE_OPENAI_MODELS = False