from pypdf import PdfReader

reader = PdfReader("6001149485.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()


file1 = open(
    r"C:\Users\danie\.code\FORT_WORTH_GASKET_AND_SUPPLY_PROJECT\\test.txt", "a")
file1.writelines(text)
