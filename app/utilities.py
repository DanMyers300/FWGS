import os
import subprocess
from flask import jsonify

BASE_URL = os.environ.get('BASE_URL', 'http://localhost:11434')
model = os.environ.get("MODEL", "llama2:7b-chat")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))

def pull_model():
    url = f"{BASE_URL}/api/pull"
    data = {
        "name": model
    }

    response = requests.post(url, json=data)

    # Check the response status
    if response.status_code == 200:
        print("Model pulled.")
    else:
        print(f"Failed to pull model. Status code: {response.status_code}")