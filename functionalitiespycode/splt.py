from PyPDF2 import PdfFileWriter, PdfFileReader
def split(inp_path,startpage,endpage):
    """
    This Function split the given pdf file with the given range and stored into first_page.pdf

    Paramters
    ---------
    inp_path(string):path of the pdf file to be splitted.
    startpage(int):page number from where we start splitting.
    endpage(int):page number upto which we will split.

    Returns
    -------
    Nothing, file is splitted and stored direcctly into first_page.pdf
    """
    
    input_pdf = PdfFileReader(inp_path)
    output = PdfFileWriter()
    for i in range(startpage,endpage+1):
        output.addPage(input_pdf.getPage(i))
        with open("first_page.pdf", "wb") as output_stream:
            output.write(output_stream)

#split('file_a.pdf',1,4)
