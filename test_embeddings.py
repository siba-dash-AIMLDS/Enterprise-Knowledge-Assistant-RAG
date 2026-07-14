from src.loader import PDFLoader
from src.chunker import DocumentChunker
from src.embeddings import EmbeddingGenerator

loader = PDFLoader()
documents = loader.load_documents()

chunker = DocumentChunker()
chunks = chunker.split_documents(documents)

embedding_generator = EmbeddingGenerator()

embeddings = embedding_generator.generate_embeddings(chunks)

print("=" * 60)
print(f"Total Chunks      : {len(chunks)}")
print(f"Embedding Vectors : {len(embeddings)}")
print(f"Embedding Size    : {len(embeddings[0])}")
print("=" * 60)