import pypdf

# create file object variable
# opening method will be rb
pdffileobj = open('6001149485.pdf', 'rb')

# create reader variable that will read the pdffileobj
pdfreader = pypdf.PdfReader(pdffileobj)

# This will store the number of pages of this pdf file
x = pdfreader.numPages

# create a variable that will select the selected number of pages
pageobj = pdfreader.getPage(x+1)

# (x+1) because python indentation starts with 0.
# create text variable which will store all text datafrom pdf file
text = pageobj.extractText()

# save the extracted data from pdf to a txt file
# we will use file handling here
# dont forget to put r before you put the file path
# go to the file location copy the path by right clicking on the file
# click properties and copy the location path and paste it here.
# put "\\your_txtfilename"
file1 = open(
    r"C:\Users\danie\.code\FORT_WORTH_GASKET_AND_SUPPLY_PROJECT\\test.txt", "a")
file1.writelines(text)
