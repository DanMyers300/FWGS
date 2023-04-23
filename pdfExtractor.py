import aspose.pdf as pdf

# Load the license
license = pdf.License()
license.set_license("Aspose.Total.lic")

# Load input PDF document
document = pdf.Document("6001149485.pdf")

# Initialize TextAbsorber object
textAbsorber = pdf.text.TextAbsorber()

# Call Page.Accept() method to fetch text
document.pages.accept(textAbsorber)

# Get the extracted text string
text = textAbsorber.text

# Create a TXT file and write the string
text_file = open("PDFtoTXT.txt", "wt")
n = text_file.write(text)
text_file.close()

print("Conversion Completed Successfully")
