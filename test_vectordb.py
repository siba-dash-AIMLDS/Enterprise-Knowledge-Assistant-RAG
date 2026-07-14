from src.loader import PDFLoader
from src.chunker import DocumentChunker
from src.vectordb import VectorDatabase

loader = PDFLoader()
documents = loader.load_documents()

chunker = DocumentChunker()
chunks = chunker.split_documents(documents)

vectordb = VectorDatabase()

db = vectordb.create_vector_db(chunks)

vectordb.save_vector_db(db)

print("=" * 60)
print("FAISS Database Created Successfully")
print("=" * 60)