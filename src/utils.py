import os

from src.const import DOWNLOAD_DIR

download_list=[]

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


def file_metadata_extractor(filename: str):
    return {'name': filename[:filename.rfind('.')]}


def get_llm():
    pass