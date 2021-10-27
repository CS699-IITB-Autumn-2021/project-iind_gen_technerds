from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

#for compression
from pylovepdf.ilovepdf import ILovePdf
#for merging
from PyPDF2 import PdfFileMerger
#for splitting
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from zipfile import ZipFile
#for word to pdf and pdf to word
import os
import comtypes.client
import time
from django.apps import apps

# Create your views here.
def index(request):
    '''
    This function is base function which render to index.html

    Parameters
    ------------
    request: GET

    Returns
    ------------
    "index.html"

    '''
    return render(request, 'index.html')

def compress(request):
    '''
    This function performs compression of pdf

    Parameters
    ------------
    request: GET / POST

    Returns
    ------------
    "compress.html": if request methos is GET
    "download-page-compress.html": if request method is POST
    '''

    if request.method == "POST":
        #delete all files that are on server
        path = apps.get_app_config('PDFMaster_App').path
        path = path.split("\\")
        path = path[:-1]
        path = "/".join(path)
        path = path+"/media/"
        print(path)
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))

        #save the file on server
        uploaded_file = request.FILES['doct']
        fs = FileSystemStorage()
        filename = fs.save (uploaded_file.name, uploaded_file)
        fileurl = fs.url(filename)
        print(fileurl)

        #compression
        #object of ilovepdf api is created
        ilovepdf_object = ILovePdf('project_public_acea6791941b90040052bcfa605303c5_4zSbs98325f7c19dfbc3987d56ed81421ab8a', verify_ssl=True)
        #compress task of api is called
        task = ilovepdf_object.new_task('compress')
        #add file to compress
        task.add_file('media/'+uploaded_file.name)
        #set output folder
        task.set_output_folder('./media')
        #given file will now will compress
        task.execute()
        #compressed file will be downloaded in media
        a=task.download()
        task.delete_current_task()

        #url of compressed file
        fileurl = 'media/'+a
        return render(request, 'download-page-compress.html', {"fileurl":fileurl})
    else:
        print(request.method)
    return render(request, 'compress.html')

def compress_download(request):
    '''
    This function renders to the page from where user can download compressed file

    Parameters
    ------------
    request: GET

    Returns
    ------------
    "download-page-compress.html"
    '''
    return render(request, 'download-page-compress.html')

def merge(request):
    '''
    This function performs merging of pdfs

    Parameters
    ------------
    request: GET / POST

    Returns
    ------------
    "merge.html": if request methos is GET
    "download-page-merge.html": if request method is POST
    '''

    if request.method == "POST":
        #delete all files that are on server
        path = apps.get_app_config('PDFMaster_App').path
        path = path.split("\\")
        path = path[:-1]
        path = "/".join(path)
        path = path+"/media/"
        print(path)
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))

        #save the files on server
        myfile = request.FILES.getlist("doct")
        print(myfile)
        pdfs=[]
        for file in myfile:
            fs=FileSystemStorage()
            filename = fs.save(file.name, file)
            pdfs.append('media/'+filename)
            fileurl = fs.url(filename)
            print(fileurl)

        #merging
        merger = PdfFileMerger()
        #iterate over all pdf path given and append it to merge object
        for pdf in pdfs:
            merger.append(pdf)
        #All pdf will be merged and merged output is written in merged.pdf file
        merger.write("media/"+"merged.pdf")
        print("DONE")
        merger.close()

        #url of merged file
        fileurl = 'media/merged.pdf'
        return render(request, 'download-page-merge.html', {"fileurl":fileurl})
    else:
        print(request.method)
    return render(request, 'merge.html')

def merge_download(request):
    '''
    This function renders to the page from where user can download compressed file

    Parameters
    ------------
    request: GET

    Returns
    ------------
    "download-page-merge.html"
    '''
    return render(request, 'download-page-merge.html')

def split(request):
    '''
    This function performs splitting of pdf

    Parameters
    ------------
    request: GET / POST

    Returns
    ------------
    "split.html": if request methos is GET
    "download-page-split.html": if request method is POST
    '''
    if request.method == "POST":
        #delete all files that are on server
        path = apps.get_app_config('PDFMaster_App').path
        path = path.split("\\")
        path = path[:-1]
        path = "/".join(path)
        path = path+"/media/"
        print(path)
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))

        #save the file on server
        uploaded_file = request.FILES['doct']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        fileurl = fs.url(filename)
        print(fileurl)

        #get values of all ranges
        range1 = [request.POST['range1']]
        range2 = [request.POST['range2']]
        range1.extend(request.POST.getlist('extra_range1'))
        range2.extend(request.POST.getlist('extra_range2'))
        print(range1)
        print(range2)

        #len(range1) should be equal to len(range2)
        if len(range1)!=len(range2):
            messages.warning(request, "Please provide sufficient range values")
            return HttpResponseRedirect(reverse_lazy('split'))

        #range 1 should be less than range 2
        for r in range(len(range1)):
            if int(range1[r])>int(range2[r]):
                messages.warning(request, "Invalid range")
                return HttpResponseRedirect(reverse_lazy('split'))

        #splitting
        inp_path="media/"+filename
        input_pdf = PdfFileReader(inp_path)

        #find maximum number of pages in pdf
        max_range = input_pdf.getNumPages()
        #range 2 must be less than maximum number of pages
        #If it is not the case, then throw the warning msg
        for r in range2:
            if int(r) > max_range:
                messages.warning(request, "Range 2 exceeds maximum range in your file")
                return HttpResponseRedirect(reverse_lazy('split'))

        split_files=[]
        #iterate over all pages in given range and write that page in required pdf file
        for r in range(len(range1)):
            startpage=int(range1[r])-1
            endpage=int(range2[r])-1
            save_as="media/split"+str(r)+".pdf"
            split_files.append(save_as)
            output = PdfFileWriter()
            for i in range(startpage,endpage+1):
                output.addPage(input_pdf.getPage(i))
                with open(save_as, "wb") as output_stream:
                    output.write(output_stream)
            output_stream.close()

        #get value of checkbox
        merging = request.POST.get('merging')
        #print(merging)
        #if checkbox is ticked, perform merging of splitted files
        if merging:
            #merging
            merger = PdfFileMerger()
            for pdf in split_files:
                merger.append(pdf)
            merger.write("media/"+"splitted.pdf")
            merger.close()
            #reset url
            fileurl = 'media/splitted.pdf'
        else:
            #create zip file if there are more than 1 splitted files
            if len(range1)>1:
                #create one zip file for all splits
                with ZipFile("media/splitted.zip",'w') as zipObj:
                    for s in split_files:
                        zipObj.write(s)
                #url of zip file which has splitted files
                fileurl="media/splitted.zip"
            else:
                #url of single splitted file
                fileurl="media/split0.pdf"
        return render(request, 'download-page-split.html', {"fileurl": fileurl})
    else:
        print(request.method)
    return render(request, 'split.html')

def split_download(request):
    '''
    This function renders to the page from where user can download splitted files

    Parameters
    ------------
    request: GET

    Returns
    ------------
    "download-page-split.html"
    '''
    return render(request, 'download-page-split.html')

def p2w(request):
    '''
    This function performs pdf to word conversion

    Parameters
    ------------
    request: GET / POST

    Returns
    ------------
    "pdf-to-word.html": if request methos is GET
    "download-page-p2w.html": if request method is POST
    '''
    if request.method == "POST":
        #delete all files that are on server
        path = apps.get_app_config('PDFMaster_App').path
        path = path.split("\\")
        path = path[:-1]
        path = "/".join(path)
        path = path+"/media/"
        print(path)
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))

        #save the file on server
        uploaded_file = request.FILES['doct']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        fileurl = fs.url(filename)
        print(fileurl)

        #pdf to word conversion
        #It Specifies the format to use when saving a document and 16 is for docx format.
        wdFormatPDF = 16

        # absolute path is needed
        # be careful about the slash '\', use '\\' or '/' or raw string r"..."
        #get absolute path of 'PDFMaster' project
        path = apps.get_app_config('PDFMaster_App').path
        path = path.split('\\')
        path = path[:-1]
        path = "\\".join(path)

        #absolute path of input pdf file
        in_file = path+"\\media\\"+filename
        #absolute path of outpur word file
        out_file = path+"\\media\\"+"pdf2word.docx"
        # print out filenames
        print(in_file)
        print(out_file)

        # create COM object
        comtypes.CoInitialize()
        # create word application object
        word = comtypes.client.CreateObject('Word.Application')
        # key point 1: make word visible before open a new document
        word.Visible = True
        # key point 2: wait for the COM Server to prepare well.
        time.sleep(3)

        # convert docx file to pdf file
        doc=word.Documents.Open(in_file) # open docx file
        doc.SaveAs(out_file, FileFormat=wdFormatPDF) # conversion
        doc.Close() # close docx file
        word.Visible = False
        word.Quit() # close Word Application

        #url word file generated
        fileurl = "media/pdf2word.docx"
        return render(request, 'download-page-p2w.html', {"fileurl": fileurl})
    else:
        print(request.method)
    return render(request, 'pdf-to-word.html')

def p2w_download(request):
    '''
    This function renders to the page from where user can download word file created from uploaded pdf file

    Parameters
    ------------
    request: GET

    Returns
    ------------
    "download-page-p2w.html"
    '''
    return render(request, 'download-page-p2w.html')

def w2p(request):
    '''
    This function performs word to pdf conversion

    Parameters
    ------------
    request: GET / POST

    Returns
    ------------
    "word-to-pdf.html": if request methos is GET
    "download-page-w2p.html": if request method is POST
    '''
    if request.method == "POST":
        #delete all files that are on server
        path = apps.get_app_config('PDFMaster_App').path
        path = path.split("\\")
        path = path[:-1]
        path = "/".join(path)
        path = path+"/media/"
        print(path)
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))

        #save the file on server
        uploaded_file = request.FILES['doct']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        fileurl = fs.url(filename)
        print(fileurl)

        #It Specifies the format to use when saving a document and 17 is for pdf format.
        wordFormatPDF = 17

        # absolute path is needed
        # be careful about the slash '\', use '\\' or '/' or raw string r"..."
        #get absolute path of 'PDFMaster' project
        path = apps.get_app_config('PDFMaster_App').path
        path = path.split('\\')
        path = path[:-1]
        path = "\\".join(path)

        #absolute path of input docx file
        in_file = path+"\\media\\"+filename
        #absolute path of outputpdf file
        out_file = path+"\\media\\"+"word2pdf.pdf"

        # print out filenames
        print(in_file)
        print(out_file)

        # Initialize COM object
        comtypes.CoInitialize();
        # create word application object
        word_object = comtypes.client.CreateObject('Word.Application')
        word_object.Visible = True
        time.sleep(3)
        # convert the given docx file  to pdf file
        document = word_object.Documents.Open(in_file) # open docx file 1
        document.SaveAs(out_file, FileFormat=wordFormatPDF)
        document.close()
        word_object.Visible = False
        word_object.Quit() # close Word Application

        #url of pdf file generated
        fileurl = "media/word2pdf.pdf"
        return render(request, 'download-page-w2p.html', {"fileurl":fileurl})
    else:
        print(request.method)
    return render(request,'word-to-pdf.html')

def w2p_download(request):
    '''
    This function renders to the page from where user can download pdf file created from uploaded word file

    Parameters
    ------------
    request: GET

    Returns
    ------------
    "download-page-w2p.html"
    '''
    return render(request,'download-page-w2p.html')

def pdf_reader(request):
    '''
    This function performs pdf reading

    Parameters
    ------------
    request: GET / POST

    Returns
    ------------
    "pdf-reader.html": if request methos is GET
    "read-pdf-page.html": if request method is POST
    '''
    if request.method == "POST":
        #delete all files that are on server
        path = apps.get_app_config('PDFMaster_App').path
        path = path.split("\\")
        path = path[:-1]
        path = "/".join(path)
        path = path+"/media/"
        print(path)
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))

        #save the file on server
        uploaded_file = request.FILES['doct']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        fileurl = fs.url(filename)
        print(fileurl)

        #url of uploaded file
        return render(request, 'read-pdf-page.html', {"fileurl": fileurl})
    else:
        return render(request, 'pdf-reader.html')

def pdf_reader_page(request):
    '''
    This function renders to the page from where user can read pdf file

    Parameters
    ------------
    request: GET

    Returns
    ------------
    "read-pdf-page.html"
    '''
    return render(request, 'read-pdf-page.html')
