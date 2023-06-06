from pypdf import PdfReader

# Define the PDF files to open
pdf_files = ["data/600114XXXX.pdf", "data/6001149485.pdf", "data/6001149819.pdf"]

# Define the output text file
output_file = "corpus.txt"

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file and return as a string."""
    with open(pdf_file, "rb") as file:
        reader = PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def convert_pdfs_to_text(pdf_files, output_file):
    """Convert a list of PDF files into a single text file."""
    with open(output_file, "w", encoding="utf-8") as file:
        for pdf_file in pdf_files:
            text = extract_text_from_pdf(pdf_file)
            file.write(text)

# Call the function to convert the PDFs to text
convert_pdfs_to_text(pdf_files, output_file)
