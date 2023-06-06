"""
NER
"""

# from pypdf import PdfReader

# PDFFileName = input("Enter the name of the PDF file: ")
# PDFFileName = "/workspaces/Fort_Worth_Gasket_And_Supply_Project/" + PDFFileName
# if not PDFFileName.endswith(".pdf"):
#     PDFFileName += ".pdf"

# # Extract the information from the pdf and save it as a text file.
# reader = PdfReader(PDFFileName)

# output_file = open("output.txt", "w", encoding="utf-8")

# for page in reader.pages:
#     output_file.write(page.extract_text())
# output_file.close()

# with open("output.txt", encoding="utf-8") as file:
#     lines = [line.strip() for line in file]
#     non_empty_lines = [line for line in lines if line != ""]
