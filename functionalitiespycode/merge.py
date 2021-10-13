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
    
    pdfs = [file1,file2]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    print("DONE")
    merger.close()

#merge('file_a.pdf','file_b.pdf')
