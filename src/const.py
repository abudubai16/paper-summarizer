import os

from src.utils import get_file_path

EDGE_DRIVER_PATH = r"C:\WebDriver\edgedriver_win64\msedgedriver.exe"
WORKING_DIR = get_file_path()
DOWNLOAD_DIR = os.path.join(WORKING_DIR, 'downloads')