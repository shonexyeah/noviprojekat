import pdfplumber
pdf_file = "sample1.pdf"
tables=[]

with pdfplumber.open(pdf_file) as pdf:
    pages = pdf.pages
    for i,pg in enumerate(pages):
        tbl = pages[i].extract_tables()
        print(f'{i} --- {tbl}')