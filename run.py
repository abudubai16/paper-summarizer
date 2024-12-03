import src

from src.paper_source import download_pdf
import src.paper_source


if __name__ == '__main__':
    url = 'https://sci-hub.st/10.1109/TPWRD.2006.883000'
    download_pdf(url, 'random.pdf')
    print(src.paper_source.download_list)
    pass