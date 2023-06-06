"""
A pdf processor


-- Need to make sure it only opens the file once. Right now it's fairly inefficient
"""
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

        output_file = open("data/output.txt", "w", encoding="utf-8")

        for page in reader.pages:
            output_file.write(page.extract_text())
        output_file.close()

    def read_text_file(self):
        "Add the non empty lines to a file and a string"
        with open("data/output.txt", encoding="utf-8") as file:
            lines = [line.strip() for line in file]
            self.non_empty_lines = [line for line in lines if line != ""]
        return "\n".join(self.non_empty_lines)
  
    def write_text_file(self):
        "Write the non empty lines to a file"
        with open("data/output.txt", "w", encoding="utf-8") as file:
            file.writelines("\n".join(self.non_empty_lines))
        return None


# Run the pdf Processor
processor = PDFProcessor()
processor.get_pdf_file_name()
processor.extract_text_from_pdf()
processor.read_text_file()
processor.write_text_file()
