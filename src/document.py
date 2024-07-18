import os

from src.const import DOWNLOAD_DIR

from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SimpleNodeParser

def read_dir():
    assert len(os.listdir(DOWNLOAD_DIR)) != 0, 'There are no files in the downloads directory'
    
    reader = SimpleDirectoryReader(DOWNLOAD_DIR)
    document = reader.load_data(show_progress=True)
    
    parser = SimpleNodeParser.from_defaults(chunk_overlap=20, chunk_size=2048)

    nodes = parser.get_nodes_from_documents(documents=document)

    print(len(nodes))

    for pos, node in enumerate(nodes):
        if pos == 5:
            print(node)


if __name__ == '__main__':
    read_dir()
    pass