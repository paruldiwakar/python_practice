#PDF programs... just remove the quotes :*

import PyPDF2

#1.to open,write,rotate pdfs
'''
with open('dummy.pdf',"rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as newfile :
        writer.write(newfile)
'''  
#2.to combine to pdf files beacause my life sucks :)
'''
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf') 
    
pdf_combiner(inputs)       
'''         

#3.to watermark babies

template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open('watermarked.pdf','wb') as file:
        output.write(file)
 
