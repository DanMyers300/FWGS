import os
from chromadb.config import Settings

# Define the folder for storing database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY', 'db')

BASE_URL = os.environ.get('BASE_URL', 'https://ddca254a49d814d87a3a52871db84276c.clg07azjl.paperspacegradient.com')

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
)
