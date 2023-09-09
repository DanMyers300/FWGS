"""
1) Run pdf processor
2) Run NER applications
"""

import subprocess

def run_subprocess(command, description):
    try:
        subprocess.run(command, check=True)
        print(f"{description} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {description}: {e}")
        raise Exception(f"{description} failed")

# Run pdf_processor.py
PDF_PROCESSOR = "src/pdf_processor.py"
run_subprocess(["python", PDF_PROCESSOR], "PDF Processor")

# Run ner.py
NER = "src/runNER.py"
run_subprocess(["python", NER], "NER")

# If NER fails, an exception has already been raised in the `run_subprocess` function.
