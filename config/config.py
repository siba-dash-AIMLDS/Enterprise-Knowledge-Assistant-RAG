import os
from dotenv import load_dotenv

load_dotenv()

# Required for other Models like Azure OpenAI and not for all-MiniLM-L6-v2
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  

# ==========================================
# Application Configuration
# ==========================================

APP_NAME = "Enterprise Knowledge Assistant"

# ==========================================
# Embedding Configuration
# ==========================================

EMBEDDING_PROVIDER = "sentence_transformers"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Later
#EMBEDDING_PROVIDER = "openai"
#EMBEDDING_MODEL = "text-embedding-3-small"
# Later
#EMBEDDING_PROVIDER = "azure"
#EMBEDDING_MODEL = "my-embedding-deployment"

# ==========================================
# Chunk Configuration
# ==========================================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ==========================================
# Retrieval Configuration
# ==========================================

TOP_K = 3

# ==========================================
# Vector Database
# ==========================================

VECTOR_DB = "FAISS"

# ==========================================
# MODEL Names
# ==========================================

MODEL_NAME = "all-MiniLM-L6-v2"
# Later
#MODEL_NAME = "text-embedding-3-small"
# Or
#MODEL_NAME = "Azure Embedding Deployment"
# ==========================================

DATA_FOLDER = "data"
LOG_LEVEL=INFO