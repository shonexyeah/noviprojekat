# import PyPDF2
#
# file_path1 = 'sample2.pdf'
# pdfFileObj = open(file_path1, 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pageObj = pdfReader.getPage(0)
#
# print(pageObj.extractText())
# print(pageObj.extractText().split('\n')[0])
# print(pageObj.extractText().split('/')[0])

import tabula
pdf_path ="sample2.pdf"

dfs = tabula.read_pdf(pdf_path, pages='2')

print(dfs[0])