# Intelligent PDF Extraction
============================

### PDF extraction using NLP library SpaCy

## TO-DO:
1. Create training set
2. Train custom model

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

Requirements:
To use the PDF Processor, you need to have the following dependencies installed:
- `pypdf` library

2. ## Named Entity Recognition (NER)
---
Items that work so far:
1. Emails
2. URLS
3. Dates
4. Addresses

Items that don't work so far:
1. RFQ
2. Version Number
3. Distribution Method
4. NNS End Use
5. Purchaser Group
6. Buyer Title
7. DPAS Rating section
8. Summary of hardware section
9. APPENDICES TO HARDWARE
10. CODED NOTES
