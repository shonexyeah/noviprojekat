import os
import unittest
import pdfplumber

HERE = os.path.abspath(os.path.dirname(__file__))

class Test(unittest.TestCase):
    @classmethod
    def setup_class(self):
        path = os.path.join(HERE, "sample2.pdf")
        self.pdf = pdfplumber.open(path)

    @classmethod
    def teardown_class(self):
        self.pdf.close()

    def test_metadata(self):
        metadata = self.pdf.metadata
        assert isinstance(metadata["Title"], str)

    def test_pagecount(self):
        assert len(self.pdf.pages) == 2

    def test_page_number(self):
        assert self.pdf.pages[0].page_number == 1
        assert str(self.pdf.pages[0]) == "<Page:1>"

    def test_pagecount2(self):
        assert len(self.pdf.pages) == 2


