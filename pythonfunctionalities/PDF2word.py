import os
import comtypes.client
import time

def PDF2word(input_file_pdf,out_file_docx):
    """
    This Function converts the given PDF file to Docx(Word) file

    Parameters
    ---------
    input_file_docx(string):path of the document file to be converted
    out_file_pdf(string):output path where converted pdf file will be stored

    Returns
    -------
    Nothing,convert the file directly.
    """

    #It Specifies the format to use when saving a document and 16 is for docx format.
    wordFormatPDF = 16
    # create word application object
    word_object = comtypes.client.CreateObject('Word.Application')
    time.sleep(3)

    # convert the given docx file  to pdf file 
    document=word_object.Documents.Open(input_file_pdf)
    document.SaveAs(out_file_docx, FileFormat=wordFormatPDF)
    document.Close()
    word_object.Quit()

#https://stackoverflow.com/questions/6011115/doc-to-pdf-using-python