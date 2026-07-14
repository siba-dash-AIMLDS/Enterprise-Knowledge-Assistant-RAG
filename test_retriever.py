from src.retriever import DocumentRetriever

retriever = DocumentRetriever()

query = "What is the medical insurance coverage?"

results = retriever.search(query)

print("=" * 60)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 60)

    print("Source :", result.metadata.get("source"))

    print()

    print(result.page_content)

print("=" * 60)