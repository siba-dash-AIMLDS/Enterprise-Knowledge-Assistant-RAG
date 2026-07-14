from sentence_transformers import SentenceTransformer
from config.config import EMBEDDING_MODEL


class EmbeddingGenerator:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def get_model(self):
        return self.model

    def generate_embeddings(self, chunks):

        texts = [chunk.page_content for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings