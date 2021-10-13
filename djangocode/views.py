from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from pylovepdf.ilovepdf import ILovePdf
import subprocess
import sys
import os
from .forms import UploadFileForm
import PyPDF2
import io
import urllib.request
from datetime import date


# Imaginary function to handle an uploaded file.

# Create your views here.
def index(request):
    #return HttpResponse("hello world")
    return render(request, 'index.html')

def compress(request):
    
    if request.method == "POST":
        uploaded_file = request.FILES['doct']
        print(uploaded_file)
        fs = FileSystemStorage()
        filename,ext=str(uploaded_file).split('.')
        name = fs.save (str(uploaded_file), uploaded_file)
        #print(name)
        url = fs.url(name)
        print('http://127.0.0.1:8000'+url)
        print(os.path.exists(name))
        
        response = urllib.request.urlopen('http://127.0.0.1:8000'+url)    
        file = open('test' + ".pdf", 'wb')
        file.write(response.read())
        file.close()
        if os.path.isfile(url):
            print("File exists and is readable")
        else:
            print("Either the file is missing or not readable")
        ilovepdf = ILovePdf('project_public_38b3ce7f045cce26af4788599d0b86b7_jwnijcf52e52d6ed850f0e797ebf4c4fea348', verify_ssl=True)
        task = ilovepdf.new_task('compress')

        task.add_file('test.pdf')
        task.set_output_folder('C:/Users/Heta/Downloads')
        task.execute()
        task.download()
        task.delete_current_task()
        today = date.today()
        d4 = today.strftime("%d-%m-%Y")
        url_download='C:/Users/Heta/Downloads'+d4
        return redirect('/compress_download',{'fileurl':url_download})

    else:
        print(request.method)
    return render(request, 'compress.html')
def compress_download(request):
    return render(request, 'download-page-compress.html')
