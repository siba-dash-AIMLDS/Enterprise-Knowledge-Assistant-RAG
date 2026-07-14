from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:
    """
    Loads all PDF documents from the data folder.
    """

    def __init__(self, data_folder: str = "data"):
        self.data_folder = Path(data_folder)

    def load_documents(self):
        documents = []

        pdf_files = list(self.data_folder.glob("*.pdf"))

        if not pdf_files:
            print("No PDF files found.")

        for pdf in pdf_files:
            print(f"Loading: {pdf.name}")

            loader = PyPDFLoader(str(pdf))
            docs = loader.load()

            documents.extend(docs)

        return documents