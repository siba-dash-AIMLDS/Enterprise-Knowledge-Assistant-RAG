from langchain_community.vectorstores import FAISS
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from config.config import EMBEDDING_MODEL


class VectorDatabase:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

    def create_vector_db(self, chunks):

        vector_db = FAISS.from_documents(
            documents=chunks,
            embedding=self.embedding_model
        )

        return vector_db

    def save_vector_db(self, vector_db, path="vectorstore"):

        vector_db.save_local(path)

        print(f"Vector database saved to '{path}'")