from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time


EDGE_DRIVER_PATH = r"C:\WebDriver\edgedriver_win64\msedgedriver.exe"
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')
os.chdir(DOWNLOAD_DIR)
download_list = []

def rename_file(save_name):
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


def download_pdf(url, file_name):
    prefs = {
        "download.default_directory": DOWNLOAD_DIR,  # Change this to your desired directory
        "download.prompt_for_download": False,
        "profile.default_content_settings.popups": 0
    }    

    edge_options = Options()
    edge_options.add_experimental_option('prefs', prefs)
    # edge_options.add_argument('--headless')

    edge_service = Service(executable_path=EDGE_DRIVER_PATH)

    driver = webdriver.Edge(service=edge_service, options=edge_options)
    
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
        time.sleep(5)

        rename_file(save_name=file_name)
        
    except TimeoutException as e:
        print("Timeout while waiting for the element:", e)
    finally:
        driver.quit()
  

if __name__ == '__main__':
    url = 'https://sci-hub.st/10.1109/TPWRD.2006.883000'
    download_pdf(url, 'random.pdf')
    pass