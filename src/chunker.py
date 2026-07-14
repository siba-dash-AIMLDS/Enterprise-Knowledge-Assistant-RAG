#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.config import CHUNK_SIZE, CHUNK_OVERLAP

class DocumentChunker:
    """
    Splits LangChain Documents into smaller chunks.
    """

    def __init__(
        self,
        #chunk_size: int = 1000,
        #chunk_overlap: int = 200,
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

    def split_documents(self, documents):

        chunks = self.text_splitter.split_documents(documents)

        return chunks