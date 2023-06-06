"""
A pdf processor


-- Need to make sure it only opens the file once. Right now it's fairly inefficient
"""
import re
from pypdf import PdfReader

class PDFProcessor:
    "Object made to process PDFs"

    def __init__(self):
        self.pdf_file_name = None
        self.non_empty_lines = None

    def get_pdf_file_name(self):
        "Get the name of the file from the user"
        self.pdf_file_name = input("Enter the name of the PDF file: ")
        # pylint: disable=C0301
        self.pdf_file_name = (
            "/workspaces/Fort_Worth_Gasket_And_Supply_Project/data/"
            + self.pdf_file_name
        )
        if not self.pdf_file_name.endswith(".pdf"):
            self.pdf_file_name += ".pdf"

    def extract_text_from_pdf(self):
        "Extract the text"
        reader = PdfReader(self.pdf_file_name)

        output_file = open("../data/output.txt", "w", encoding="utf-8")

        for i, page in enumerate(reader.pages):
            if i + 1 not in [2, 3, 4]:  # Skip pages 2, 3, and 4
                text = page.extract_text()
                text = re.sub(r"\n+", " ", text)  # Replace multiple newline characters with spaces
                text = re.sub(r"^\s*\n", "", text, flags=re.MULTILINE)  # Remove blank lines

                output_file.write(text)

        output_file.close()

# Run the pdf Processor
processor = PDFProcessor()
processor.get_pdf_file_name()
processor.extract_text_from_pdf()
