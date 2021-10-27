from PyPDF2 import PdfFileMerger
def merge(file1,file2):
    """
    This Function Merge the given pdf file and output merged pdf in result.pdf

    Paramters
    ---------
    file1(string):path of the 1st pdf file to merge 
    file2(string):path of the 2nd pdf file to merge

    Returns
    -------
    Nothing,Merged file is Writed directly into result.pdf.
    """
    
    list_pdf = [file1,file2]
    merger = PdfFileMerger()
    #iterate over all pdf path given and append it to merge object
    for pdf_path in list_pdf:
        merger.append(pdf_path)

    #All pdf will be merged and merged output is writte in result.pdf file    
    merger.write("result.pdf")
    merger.close()
#https://stackoverflow.com/questions/3444645/merge-pdf-files