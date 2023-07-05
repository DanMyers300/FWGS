"""
NER
"""
import re
import json
import spacy
import pyap
from spacy.matcher import Matcher

#
# --- Open file and load spaCy --- #
#

def open_file():
    "Open corpus of text"
    with open(
        "data/corpus.txt",
        "r",
        encoding="utf-8",
    ) as file:
        contents = file.read()
    return contents
corpus = open_file()
nlp = spacy.load("en_core_web_lg")
doc = nlp(corpus)

#
# --- Define entities to extract --- #
#

class Emails:
    "Extract emails from text"

    def __init__(self):
        self.email_pattern = [{"LIKE_EMAIL": True}]
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add("EMAIL_ADDRESS", [self.email_pattern])
        self.email_matches = None

    def extract_emails(self, output_file):
        "Extract emails then dump to json"
        self.email_matches = self.matcher(doc)
        results = []
        for match in self.email_matches[:10]:
            email_address = str(doc[match[1]])
            results.append({"label": "email", "text": email_address})

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(results, file)


class URLs:
    "extract URLs from text"

    def extract_urls(self, output_file):
        "Parse URLs from text"
        urls = []
        for token in doc:
            if token.like_url:
                urls.append({"label": "URL", "text": token.text})
        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(urls, file)
        return urls


class Dates:
    "Extract dates"

    def __init__(self):
        self.dates = []
        self.pattern = r"\b(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[01])/(\d{4})\b"

    def extract_dates(self, output_file):
        "Parse dates from text"
        matcher = Matcher(nlp.vocab)
        pattern_list = [[{"TEXT": {"REGEX": self.pattern}}]]
        matcher.add("DATE", pattern_list)
        matches = matcher(doc)

        for match in matches:
            _, start, end = match
            span = doc[start:end]
            date = {"label": "DATE", "text": span.text}
            self.dates.append(date)

        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(self.dates, file)

        return self.dates


class Addresses:
    "Extract addresses from text"

    def extract_addresses(self, output_file):
        "Extract addresses"
        addresses = pyap.parse(corpus, country='US')
        results = []
        for address in addresses:
            if "ONE INTERNATIONAL INC" not in str(address):
                result = {
                    'address': str(address),
                    'address_parts': address.as_dict()
                }
                results.append(result)

        # Save results to a JSON file
        with open(
                 output_file, 
                 'w',
                 encoding="utf-8"
                 ) as file:
            json.dump(results, file, indent=4)

class RFQ:
    def extract_rfq(self, model_path, addresses_file, output_file):
        rfq_nlp = spacy.load(model_path)
        rfq_doc = rfq_nlp(corpus)
        
        with open(addresses_file, 'r', encoding="utf-8") as file:
            addresses = json.load(file)

        entities = []
        for ent in rfq_doc.ents:
            if ent.text.isalnum() and not ent.text.isalpha():  # Select alphanumeric entities with at least one digit
                is_street_number = False
                for address in addresses:
                    if ent.text == address['address_parts']['street_number']:
                        is_street_number = True
                        break
                if not is_street_number or len(ent.text) > len(address['address_parts']['street_number']):
                    entities.append({'text': ent.text, 'label': ent.label_})

        with open(output_file, 'w', encoding="utf-8") as file:
            json.dump(entities, file, indent=4)


class CODED_NOTES:
    def extract_coded_notes(self, input_file, output_file):
        codes = []
        
        with open(input_file, 'r') as file:
            lines = file.readlines()[1:]  # Skip the header line
            for line in lines:
                code = line.split(',')[0]
                codes.append(code.strip())

        # Remove "APPENDICES" from the list
        codes = [code for code in codes if code != "APPENDICES"]

        # Extract the codes from rfq_dump.txt
        extracted_codes = []
        for code in codes:
            matches = re.findall(code, corpus)
            extracted_codes.extend(matches)
        
        # Write extracted_codes to coded_notes.json
        with open(output_file, 'w') as output_file:
            json.dump(extracted_codes, output_file)

#
# --- Run the extraction --- #
#

#------------------------------

#Emails().extract_emails(
#   "data/outputs/emails.json"
#)

#------------------------------

#URLs().extract_urls(
#        "data/outputs/urls.json"
#)

#------------------------------

#Dates().extract_dates(
#        "data/outputs/dates.json",
#)

#------------------------------

#Addresses().extract_addresses(
#        "data/outputs/addresses.json",
#)

#------------------------------

#RFQ().extract_rfq(
#        "data/models/rfq_model/model-best",
#        "data/outputs/addresses.json",
#        "data/outputs/rfq.json",
#)

#------------------------------

#CODED_NOTES().extract_coded_notes(
#        "data/base_files/csv/coded_notes.csv",
#        "data/outputs/coded_notes.json",
#)

#------------------------------

