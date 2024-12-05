import os
import shutil

from src.utils import file_metadata_extractor, get_dirs
from src.const import DOWNLOAD_DIR

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SimpleNodeParser, SemanticSplitterNodeParser
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage

import shutil  # For directory deletion


class IndexManager:
    """
        Manages saving, loading, and deleting indexes for a specific paper.
        If the index directory is empty, it creates an index from the downloaded documents.
    """

    def __init__(self, paper_name: str):
        self.paper_name = paper_name
        self.dirs = get_dirs(paper_name)
        self.index_path = self.dirs['index']
        if len(os.listdir(self.index_path))==0:
            self.create_index()


    def create_index(self):
        """
            - Create and save an index if the download directory is not empty.
        """
        assert len(os.listdir(DOWNLOAD_DIR)) != 0, 'There are no files in the downloads directory to ingest'

        reader = SimpleDirectoryReader(DOWNLOAD_DIR, file_metadata=file_metadata_extractor)
        documents = reader.load_data(show_progress=True)

        print('Generating Index!')

        parser = SemanticSplitterNodeParser(
            buffer_size=1,
            breakpoint_percentile_threshold=95,
            embed_model=OpenAIEmbedding()
        )
        nodes = parser.get_nodes_from_documents(documents=documents, show_progress=True)

        index = VectorStoreIndex(nodes)
        index.storage_context.persist(persist_dir=self.index_path)


    def load_index(self):
        """
            - Loads an index from the specified directory.
        """
        if not os.path.exists(self.index_path):
            raise FileNotFoundError(f"No index found at {self.index_path}")

        storage_context = StorageContext.from_defaults(persist_dir=self.index_path)
        index = load_index_from_storage(storage_context=storage_context)
        return index


    def delete_index(self) -> None:
        """
        Delete the index directory and its contents.
        """
        shutil.rmtree(self.index_path)
