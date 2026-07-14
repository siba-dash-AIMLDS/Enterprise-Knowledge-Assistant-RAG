import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Chunking Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

DATA_FOLDER = "data"

# Vector DBs
VECTOR_DB = "faiss"

# Today/Now
MODEL_NAME = "all-MiniLM-L6-v2"
# Later
#MODEL_NAME = "text-embedding-3-small"
# Or
#MODEL_NAME = "Azure Embedding Deployment"

# # Embedding Configuration Today/Now
EMBEDDING_PROVIDER = "sentence_transformers"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
# Later
#EMBEDDING_PROVIDER = "openai"
#EMBEDDING_MODEL = "text-embedding-3-small"
# Later
#EMBEDDING_PROVIDER = "azure"
#EMBEDDING_MODEL = "my-embedding-deployment"