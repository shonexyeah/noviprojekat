### PDF MINER SECTION ###

import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()

            converter = TextConverter(resource_manager,
                                      fake_file_handle)

            page_interpreter = PDFPageInterpreter(resource_manager,
                                                  converter)

            page_interpreter.process_page(page)
            text = fake_file_handle.getvalue()

            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()


def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        print(page)
        print()

    # Driver code


if __name__ == '__main__':
    print(extract_text('sample2.pdf'))

#### PDF PLUMBER SECTION ####

import pdfplumber


def meta_data():
    pdf = pdfplumber.open("sample2.pdf")

    print("Number of pages: {}".format(len(pdf.pages)))
    print("Pages : {}".format(pdf.pages))

    print("Document Information")
    print(pdf.metadata)

    print("Author name : {}".format(pdf.metadata["Author"]))
    print("Creator : {}".format((pdf.metadata["Creator"])))


def extract_first():
    pdf = pdfplumber.open("sample2.pdf")
    page = pdf.pages[0]
    text = page.extract_text()

    print("First page data : {}".format(text))
    pdf.close()


def extract_whole():
    pdf = pdfplumber.open("sample2.pdf")
    n = len(pdf.pages)

    final = ""
    for page in range(n):
        data = pdf.pages[page].extract_text()
        final = final + "\n" + data

    print("Whole document data : {}".format(final))

### PyPDF2 SECTION ###

from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'sample2.pdf'
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

