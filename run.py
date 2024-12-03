from pdb import run
import src

from src.setup import run_setup
from src.paper_source import download_doi, download_pdf
import src.paper_source

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
    pass

if __name__ == '__main__':
    run_application_testing()
    pass