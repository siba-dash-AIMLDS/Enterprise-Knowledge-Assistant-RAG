from langchain_community.vectorstores import FAISS
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from config.config import EMBEDDING_MODEL


class DocumentRetriever:

    def __init__(self):

        embedding = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        self.db = FAISS.load_local(
            "vectorstore",
            embedding,
            allow_dangerous_deserialization=True
        )

    def search(self, query, k=3):

        return self.db.similarity_search(query, k=k)