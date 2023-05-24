"""
Set up all dependencies then run main.py
"""

import subprocess
import sys


def install_dependencies():
    """Run pip to install the requirements from the requirements.txt file"""
    # subprocess.check_call(
    #     [sys.executable, "pip", "install", "-r", "requirements.txt"]
    # )
    # Run the command to download the language model
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_lg"])


def run_main():
    """
    Runs main function
    """
    # Execute your main.py file
    subprocess.check_call([sys.executable, "/workspaces/Fort_Worth_Gasket_And_Supply_Project/NER/pdf_ner_extraction/main.py"])


if __name__ == "__main__":
    install_dependencies()
    run_main()
