import os
import time

from src.const import DOWNLOAD_DIR

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Automatically manage the driver
from webdriver_manager.chrome import ChromeDriverManager


if not os.path.exists(DOWNLOAD_DIR):
    os.mkdir(DOWNLOAD_DIR)
os.chdir(DOWNLOAD_DIR)
download_list = []


# Check if the file is downloaded or not, if it is then rename
def rename_file(save_name:str)-> None:
    dir_list = os.listdir(DOWNLOAD_DIR)
    file_found = False
    for file in dir_list:
        if file not in download_list:
            print('File Downloaded!')
            os.rename(file, save_name)
            file_found = True

            download_list.append(save_name)
            break

    if file_found:
        print('File renamed!')
    else:
        print('File Not Downloaded')


def download_pdf(url:str, file_name:str)-> None:
    prefs = {
        "download.default_directory": DOWNLOAD_DIR, 
        "download.prompt_for_download": False,
        "profile.default_content_settings.popups": 0
    }

    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--headless')  
    chrome_options.add_argument('--disable-gpu')

    # Manage the webdriver automatically
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        driver.get(url)
        driver.delete_all_cookies()
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print('Website opened!!!')

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '↓ save')]"))
        ).click()
        print('Save button clicked!')

        time.sleep(5)
        rename_file(save_name=file_name)
        
    except TimeoutException as e:
        print("Timeout while waiting for the element:", e)
    finally:
        driver.quit()
  

def download_doi(doi: str, file_name: str)-> None:
    download_pdf(f'https://sci-hub.st/{doi}', file_name)
    return 


if __name__ == '__main__':
    pass