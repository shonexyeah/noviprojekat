import os
import requests #pip install requests
from PyPDF2 import PdfFileReader, PdfFileWriter
import pdfplumber

urls = [
    'https://www.africau.edu/images/default/sample.pdf',
]

output_dir = './'

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(output_dir, os.path.basename(url))
        with open(file_path, 'wb') as f:
            f.write(response.content)


file_path = 'sample.pdf'
pdf = PdfFileReader(file_path)

with open('Sample Note.txt', 'w') as f:
    for page_num in range(pdf.numPages):
        print('Page: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()


pdf = pdfplumber.open('sample.pdf')
page = pdf.pages[0]
text = page.extract_text()
print(text)