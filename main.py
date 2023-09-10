"""
1) Run pdf processor
2) Run NER applications
"""
from src.pdf_processor import PDFProcessor
from src.runNER import EMAILS, URLs, DATES, ADDRESSES, RFQ, CODED_NOTES, COMBINE_OUTPUTS


spacy.cli.download("en_core_web_lg")

# Run pdf_processor.py
processor = PDFProcessor()
processor.get_pdf_file_names()
processor.extract_text_from_pdf()

#
# --- Run the extraction --- #
#

EMAILS().extract_emails(
   "data/outputs/emails.json"
)
URLs().extract_urls(
        "data/outputs/urls.json"
)
DATES().extract_dates(
        "data/outputs/dates.json",
)
ADDRESSES().extract_addresses(
        "data/outputs/addresses.json",
)
RFQ().extract_rfq(
        "data/models/rfq_model/model-best",
        "data/outputs/addresses.json",
        "data/outputs/rfq.json",
)
CODED_NOTES().extract_coded_notes(
        "data/base_files/csv/coded_notes.csv",
        "data/outputs/coded_notes.json",
)
COMBINE_OUTPUTS().combine_outputs()

