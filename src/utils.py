import os

from src.const import DOWNLOAD_DIR, DEFAULT_PROMPT_LOC, INDEXES_DIR

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


def load_prompts(prompt_loc=DEFAULT_PROMPT_LOC)->str:
    """
        All files must be in the prompts folder and must be surrounded by triple qoutes
    """
    if not os.path.exists(prompt_loc): 
        raise FileNotFoundError(f"Prompt file not found at {prompt_loc}")
    else: 
        with open(prompt_loc, 'r') as f:
            prompt_template = f.read()
        return prompt_template


def create_index_dirs(paper_name:str, root_dir:str=INDEXES_DIR)->None:
    """
        Create the directories for the paper's index and chat history.
        Inputs: 
            - paper_name: The name of the directory containing the paper resources
            - root_dir: The root directory containing all of the papers
    """
    paper_dir = os.path.join(root_dir, paper_name)
    index_dir = os.path.join(paper_dir, 'index')
    chat_dir = os.path.join(paper_dir, 'chats')
    dirs = [paper_dir, index_dir, chat_dir]

    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
    
    print(f'Index directory created at {paper_dir}')


def get_dirs(paper_name:str, root_dir:str=INDEXES_DIR)->dict:
    """
        Get the directories for the paper's index and chat history.
        Inputs: 
            - paper_name: The name of the directory containing the paper resources
            - root_dir: The root directory containing all of the papers
    """
    dirs={
        'paper': os.path.join(root_dir, paper_name),
        'index': os.path.join(os.path.join(root_dir, paper_name), 'index'),
        'chats': os.path.join(os.path.join(root_dir, paper_name), 'chats')
    }

    if os.path.exists(dirs['paper']):
        return dirs
    else:
        raise FileNotFoundError(f'Paper directory not found at {dirs["paper"]}')


def get_llm():
    pass