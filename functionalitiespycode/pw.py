
from pdf2docx import Converter
from pdf2docx import parse
def pdf2doc(pdf_path,word_path):
    """
    This Function convert the given docx file into the pdf file

    Paramters
    ---------
    pdf_path(string):path of the pdf file to be converted to word file.
    word_path(string): path to which converted word file is stored.

    Returns
    -------
    Nothing,word file is directly converted.
    """
    parse(pdf_path, word_path, start=0, end=None)

#pdf2doc('first_page.pdf','p2w.docx')

