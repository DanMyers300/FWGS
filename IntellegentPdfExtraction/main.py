""" This code is to extract a pdf file and use NER to parse the important information
    Written by Daniel Myers (contact@danmyers.net)
"""
# Imports
# import re
# import spacy
# import pandas as pd
# from spacy.matcher import Matcher
from pypdf import PdfReader


# Take in user input for what the name of the pdf is.
# If it doesn't end in .pdf add it
PDFFileName = input("Enter the name of the PDF file: ")
PDFFileName = "../" + PDFFileName
if not PDFFileName.endswith(".pdf"):
    PDFFileName += ".pdf"

# Extract the information from the pdf and save it as a text file.
reader = PdfReader(PDFFileName)

output_file = open("output.txt", "w", encoding="utf-8")

for page in reader.pages:
    output_file.write(page.extract_text())
output_file.close()

with open("output.txt", encoding="utf-8") as file:
    lines = [line.strip() for line in file]
    non_empty_lines = [line for line in lines if line != ""]

mystr = ", ".join(non_empty_lines)
# print(mystr)
# Create a string variable to hold the cleaned version of the string
rmspecialchar = ""

# Define a list of special characters to remove
special_chars = ["!", ",", "#", "$", "%", "^", "&", "*", ":", ")", "("]

# Iterate over each character in the string
for char in mystr:
    # Check if the character is a special character
    if char in special_chars:
        # If it is, skip it and move on to the next character
        continue
    else:
        # If it isn't a special character, add it to the cleaned string
        rmspecialchar += char

# Print the cleaned string
print(rmspecialchar)
