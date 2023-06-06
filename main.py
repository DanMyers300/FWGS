"""
1) Run pdf processor
2) Run NER
"""
import subprocess

# Run pdf_processor.py
PDF_PROCESSOR = "./ner/pdf_processor.py"
subprocess.run(["python", PDF_PROCESSOR], check=True)

# Run ner.py
NER = "./ner/ner.py"
subprocess.run(["python", NER], check=True)
