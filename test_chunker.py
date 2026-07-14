from src.loader import PDFLoader
from src.chunker import DocumentChunker

loader = PDFLoader()

documents = loader.load_documents()

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

print("=" * 60)
print(f"Total Chunks : {len(chunks)}")
print("=" * 60)

for i, chunk in enumerate(chunks, start=1):

    print("=" * 60)
    print(f"Chunk : {i}")
    print(f"Source : {chunk.metadata.get('source')}")
    print(f"Characters : {len(chunk.page_content)}")
    print(chunk.page_content[:200])