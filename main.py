"""
1) Install requirements
2) Run pdf processor
3) Run NER
"""
import subprocess

install_requirements = input("Do you want to install the requirements? (y/n): ")

if install_requirements.lower() == "y":
    # Update Pip
    subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
    # Install requirements.txt
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

# Run pdf_processor.py
PDF_PROCESSOR = "src/pdf_processor.py"
subprocess.run(["python", PDF_PROCESSOR], check=True)

# Run ner.py
NER = "src/runNER.py"
subprocess.run(["python", NER], check=True)
