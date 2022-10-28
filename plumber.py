# import pdfplumber
#
# file = 'sample1.pdf'
#
# with pdfplumber.open(file) as pdf:
#     page = pdf.pages[0]
#     text = page.extract_text()
#     print(text)
#
#
# pdf = pdfplumber.open("sample1.pdf")
# p0 = pdf.pages[0]
# table = p0.extract_table()
# print(table)
#
# find_table = p0.find_tables()
# print(find_table)


import requests
from os.path import basename

urls = [
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn12.pdf'

]

for url in urls:
    pdf_fname = 'PDF-' + basename(url)
    print("Downloading", url, 'into', pdf_fname)
    response = requests.get(url)
    if response.status_code == 200:
        with open(pdf_fname, 'wb') as f:
            f.write(response.content)

