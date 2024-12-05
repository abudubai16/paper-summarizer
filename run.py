from src.setup import run_setup
from src.paper_source import download_doi, download_pdf

from src.utils import create_index_dirs
from src.chats import ChatManager
from src.indexes import IndexManager
from src.chat_engine import ChatEngineOpenAI


def run_application_doi()-> None:
    run_setup()
    doi = input('Enter the DOI of the paper')
    download_doi(doi, 'random.pdf')
    pass


def run_application_testing()-> None:
    run_setup()
    # Test paper to be downloaded
    url = 'https://sci-hub.st/10.1109/TPWRD.2006.883000'
    download_pdf(url, 'random.pdf')
    
    paper_name='testing'
    create_index_dirs(paper_name=paper_name)
    chat_manager = ChatManager(paper_name=paper_name)
    index_manager = IndexManager(paper_name=paper_name)
    chat_engine = ChatEngineOpenAI(index_manager=index_manager, chat_manager=chat_manager, prompt=None)
    chat_engine.run()


if __name__ == '__main__':
    run_application_testing()
    pass