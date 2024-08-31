import os

from src.const import DOWNLOAD_DIR

def check_dirs():
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)

def check_requirements():
    pass

if __name__=='__main__':
    pass