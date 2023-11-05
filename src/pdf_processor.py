"""
A pdf processor


-- Need to make sure it only opens the file once. Right now it's fairly inefficient
"""
import os
import re
from pypdf import PdfReader

class PDFProcessor:
    "Object made to process PDFs"

    def __init__(self):
        self.pdf_file_names = None
        self.non_empty_lines = None

    def get_pdf_file_names(self):
        "Get the names of all PDF files in the current directory and the 'data' folder"
        try:
            current_folder = os.getcwd()  # Get the current operating folder
            pdf_files = [
                file
                for file in os.listdir(current_folder)  # List files in the current folder
                if file.endswith(".pdf")
            ]
            data_folder = os.path.join(current_folder, "data")  # Create a path to the 'data' folder
            if os.path.exists(data_folder) and os.path.isdir(data_folder):
                data_pdf_files = [
                    os.path.join(data_folder, file)
                    for file in os.listdir(data_folder)  # List files in the 'data' folder
                    if file.endswith(".pdf")
                ]
            else:
                data_pdf_files = []
        
            self.pdf_file_names = pdf_files + data_pdf_files  # Combine the lists of PDF files
        except OSError as e:
            print(f"Error while getting PDF file names: {e}")

    def extract_text_from_pdf(self):
        "Extract the text from all PDF files"
        try:
            output_file = open(
                "data/corpus.txt",
                "w",
                encoding="utf-8",
            )

            for pdf_file in self.pdf_file_names:
                try:
                    reader = PdfReader(pdf_file)

                    for i, page in enumerate(reader.pages):
                        if i + 1 not in [2, 3, 4]:  # Skip pages 2, 3, and 4
                            text = page.extract_text()
                            text = re.sub(
                                r"\n+", " ", text
                            )  # Replace multiple newline characters with spaces
                            text = re.sub(
                                r"\s{2,}", " ", text
                            )  # Replace multiple spaces with a single space
                            text = re.sub(
                                r"^\s*\n", "", text, flags=re.MULTILINE
                            )  # Remove blank lines

                            output_file.write(text)

                except Exception as e:
                    print(f"Error processing {pdf_file}: {e}")

            output_file.close()
        except OSError as e:
            print(f"Error while writing to output file: {e}")

# Run the pdf Processor
processor = PDFProcessor()
processor.get_pdf_file_names()
processor.extract_text_from_pdf()

