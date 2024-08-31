import os

def get_file_path():
    return os.getcwd()


def file_metadata_extractor(filename: str):
    return {'name': filename[:filename.rfind('.')]}


def get_llm():
    pass

if __name__ == '__main__':
    pass