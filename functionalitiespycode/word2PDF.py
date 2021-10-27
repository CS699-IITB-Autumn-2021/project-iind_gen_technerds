import os
import comtypes.client
import time

def word2PDF(input_file_docx,out_file_pdf):
    """
    This Function converts the given document file to pdf file

    Parameters
    ---------
    input_file_docx(string):path of the pdf file to be converted
    out_file_pdf(string):output path where converted document file will be stored

    Returns
    -------
    Nothing,convert the file directly.
    """

    #It Specifies the format to use when saving a document and 17 is for pdf format.
    wdFormatPDF = 17
        
    # create word application object
    word_object = comtypes.client.CreateObject('Word.Application')
    time.sleep(3)
    #convert given pdf file to word file
    document=word_object.Documents.Open(input_file_docx)
    document.SaveAs(out_file_pdf, FileFormat=wdFormatPDF)
    document.Close()
    word_object.Quit() # close Word Application


#https://stackoverflow.com/questions/6011115/doc-to-pdf-using-python