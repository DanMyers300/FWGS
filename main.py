"""
1) Install requirements
2) Run pdf processor
3) Run NER
"""
import subprocess

# Install requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

# Run pdf_processor.py
PDF_PROCESSOR = "./ner/pdf_processor.py"
subprocess.run(["python", PDF_PROCESSOR], check=True)

# Run ner.py
NER = "./ner/ner.py"
subprocess.run(["python", NER], check=True)
