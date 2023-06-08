# Intelligent PDF Extraction
============================================================

### PDF extraction using NLP library `SpaCy`

## Usage
-----
1. Put the PDF file into the /data/ directory.
2. Run the main.py script.

## Components /ner/
----------
1. ## PDF Processor:

This program is a PDF processor designed to extract text from PDF files. It utilizes the `pypdf` library to read PDF files and extract their text content.

Description:
The PDF Processor is a Python program that allows you to extract text from PDF files and save it for further processing or analysis. It provides a convenient way to automate the extraction of text from PDF documents.

Features:
- Extracts text from PDF files
- Saves extracted text to an output file
- Removes empty lines from the extracted text

2. ## Named Entity Recognition (NER)
---
### The NER (Named Entity Recognition) component is responsible for extracting specific entities from the text using the SpaCy library.

Description:

Features:

#### Working
1. Emails
2. URLS
3. Dates
4. Addresses
5. RFQ
---
#### Not working
1. Version Number
2. Distribution Method
3. NNS End Use
4. Purchaser Group
5. Buyer Title
6. DPAS Rating section
7. Summary of hardware section
8. APPENDICES TO HARDWARE
9. CODED NOTES

3. ## Import to database
---
### To-Do