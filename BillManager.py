import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io

def pdfparser(data):

    fp = open(data, 'rb')
    newfile=open('input_tempFile.txt','w')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    newfile.write(data)
    newfile.close()

def FindTotal():
	finalfile=open('FinalFile.txt','w')
	for line in reversed(list(open("input_tempFile.txt"))):	
		if "Total" in line.rstrip():
			TempLine= line.rsplit("   ")
			finalfile.write("Total Value : " + TempLine[-2] + TempLine[-1] )
			break	
	finalfile.close()
	
def FindProducts():
	finalfile=open('FinalFile.txt','a')
	count=False
	start=False
	for line in list(open("input_tempFile.txt")):
		if ("Item" in line.rstrip()) or ("Particulars" in line.rstrip()):
			count=True
			continue
			
		if count:
			TempLine= line.rsplit("     ")
			if "---" in line.rstrip() and start:
				break
			start=True
			if len(TempLine) != 0:
				finalfile.write(TempLine[0] + "\n")
	finalfile.close()
	
	
if __name__ == '__main__':
    pdfparser(sys.argv[1]) 
	
#pass the pdf name using	
FindTotal()
FindProducts()
