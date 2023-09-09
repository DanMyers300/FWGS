"""
1) Run pdf processor
2) Run NER applications
"""

import subprocess

# Run pdf_processor.py
PDF_PROCESSOR = "src/pdf_processor.py"
subprocess.run(["python", PDF_PROCESSOR], check=True)

# Run ner.py
NER = "src/runNER.py"
subprocess.run(["python", NER], check=True)
raise Exception("NER failed")
