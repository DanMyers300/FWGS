""" This code is to extract a pdf file and use NER to parse the important information
    Written by Daniel Myers (contact@danmyers.net)
"""
import re

# import pandas as pd
from spacy.matcher import Matcher
import spacy
from pypdf import PdfReader

#           --- The following code is to convert a pdf into a string for spacy to understand it ---

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

DATA_STRING = ", ".join(non_empty_lines)
# print(mystr)
# Create a string variable to hold the cleaned version of the string
RM_SPECIAL = ""

# Define a list of special characters to remove
special_chars = [
    "!",
    ",",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    ":",
    ")",
    "(",
]

# Iterate over each character in the string
for char in DATA_STRING:
    # Check if the character is a special character
    if char in special_chars:
        # If it is, skip it and move on to the next character
        continue
    else:
        # If it isn't a special character, add it to the cleaned string
        RM_SPECIAL += char


def reduce_multiple_spaces(text):
    """Removing double spaces"""
    reduced_text = re.sub(r"\s+", " ", text)
    return reduced_text


# Example usage
INPUT = RM_SPECIAL
RM_SPACES = reduce_multiple_spaces(INPUT)


nlp = spacy.load("en_core_web_lg")
doc = nlp(RM_SPACES)
matcher = Matcher(nlp.vocab)

print(doc)

RFQ_PATTERN = r"RFQ \d+"
matches = re.finditer(RFQ_PATTERN, RM_SPACES)
for match in matches:
    print(match)

DATE_PATTERN = r"\d\d/\d\d/\d\d\d\d"
matches = re.finditer(DATE_PATTERN, RM_SPACES)
for match in matches:
    print(match)

EMAIL_PATTERN = [{"LIKE_EMAIL": True}]
matcher.add("EMAIL_ADDRESS", [EMAIL_PATTERN])
Emailmatches = matcher(doc)
for match in Emailmatches[:10]:
    print(match, doc[match[1]])

#           --- SELLER INFO ---

SELLER_ID_PATTERN = r"\d+ Seller ID"
IDMatches = re.finditer(SELLER_ID_PATTERN, RM_SPACES)
for match in IDMatches:
    print(match)

SELLER_CONTACT_PERSON_PATTERN = r"[A-Z]+ [A-Z]+ [A-Z]+ Seller Contact Person"
sellerContactPersonMatches = re.finditer(SELLER_CONTACT_PERSON_PATTERN, RM_SPACES)
for match in sellerContactPersonMatches:
    print(match)

SELLER_PHONE_NO_PATTERN = r"Seller Phone No \d+-\d+-\d+"
sellerPhoneNumberMatches = re.finditer(SELLER_PHONE_NO_PATTERN, RM_SPACES)
for match in sellerPhoneNumberMatches:
    print(match)

#           --- BUYER INFO ---

#DIDN'T WORK
BUYER_CONTACT_PATTERN = r"Purchaser Contact [A-Z, a-z]+(?= Payment)"
purchaserContactPersonMatches = re.finditer(BUYER_CONTACT_PATTERN, RM_SPACES)
for match in purchaserContactPersonMatches:
    print(match)

BUYER_PHONE_NO_PATTERN = r"Purchaser Phone No \d+-\d+-\d+"
purchaserPhoneNumberMatches = re.finditer(BUYER_PHONE_NO_PATTERN, RM_SPACES)
for match in purchaserPhoneNumberMatches:
    print(match)

# DIDN"T WORK
BUYER_ADDRESS_PATTERN = r"Purchaser Address \d+ [A-Z, a-z]+"
purchaserAddressMatches = re.finditer(BUYER_ADDRESS_PATTERN, RM_SPACES)
for match in purchaserAddressMatches:
    print(match)

BUYER_GROUP_PATTERN = r"[A-Z, a-z]+\d+ Purchaser Group"
purchaserGroupMatches = re.finditer(BUYER_GROUP_PATTERN, RM_SPACES)
for match in purchaserGroupMatches:
    print(match)

BUYER_TITLE_PATTERN = r"[A-Z]+ [A-Z]+ [A-Z]+ \d+ Buyer Title"
buyerTitleMatches = re.finditer(BUYER_TITLE_PATTERN, RM_SPACES)
for match in buyerTitleMatches:
    print(match)
