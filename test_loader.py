from src.loader import PDFLoader

loader = PDFLoader()

documents = loader.load_documents()

print("=" * 60)

print(f"Total Pages Loaded : {len(documents)}")

print("=" * 60)

for i, doc in enumerate(documents, start=1):
    print("=" * 60)
    print(f"Document : {i}")
    print(f"Source   : {doc.metadata.get('source')}")
    print(f"Page     : {doc.metadata.get('page')}")
    print(f"Characters : {len(doc.page_content)}")
    print("-" * 60)
    print(doc.page_content[:200])