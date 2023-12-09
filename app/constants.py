import os
from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()

# Define the folder for storing database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY', 'db')

BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
)
