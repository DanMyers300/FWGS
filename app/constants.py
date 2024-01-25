import os
from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()

model = os.environ.get("MODEL", "llama2:7b-chat")
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'llama2:7b')

# Define the folder for storing database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY', 'db')

BASE_URL = os.environ.get('BASE_URL', 'http://localhost:11434')

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
)