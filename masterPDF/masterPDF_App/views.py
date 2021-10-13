from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import *
# Create your views here.
def index(request):
    #return HttpResponse("hello world")
    return render(request, 'index.html')

def compress(request):
    if request.method == "POST":
        '''
        form = compressForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/compress_download')

        '''
        uploaded_file = request.FILES['doct']
        #print(upload_file.name, upload_file.size)
        fs = FileSystemStorage()
        name = fs.save (uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        return redirect('/compress_download')

    else:
        print(request.method)
        '''
        form = compressForm()
        '''
    return render(request, 'compress.html')

def compress_download(request):
    '''
    pdf = PDF.objects.all()
    return render(request, 'download-page-compress.html',{
        'uploaded_pdf':pdf
    })
    '''
    #print(_url)
    return render(request, 'download-page-compress.html')

def merge(request):
    if request.method == "POST":
        uploaded_file = request.FILES['doct']
        #print(upload_file.name, upload_file.size)
        fs = FileSystemStorage()
        name = fs.save (uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        return redirect('/merge_download')
    else:
        print(request.method)
    return render(request, 'merge.html')

def merge_download(request):
    return render(request, 'download-page-merge.html')

def split(request):
    if request.method == "POST":
        uploaded_file = request.FILES['doct']
        #print(upload_file.name, upload_file.size)
        fs = FileSystemStorage()
        name = fs.save (uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        return redirect('/split_download')
    else:
        print(request.method)
    return render(request, 'split.html')

def split_download(request):
    return render(request, 'download-page-split.html')

def p2w(request):
    if request.method == "POST":
        uploaded_file = request.FILES['doct']
        #print(upload_file.name, upload_file.size)
        fs = FileSystemStorage()
        name = fs.save (uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        return redirect('/p2w_download')
    else:
        print(request.method)
    return render(request, 'pdf-to-word.html')

def p2w_download(request):
    return render(request, 'download-page-p2w.html')

def w2p(request):
    if request.method == "POST":
        uploaded_file = request.FILES['avatar']
        #print(upload_file.name, upload_file.size)
        fs = FileSystemStorage()
        name = fs.save (uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        return redirect('/w2p_download')
    else:
        print(request.method)
    return render(request,'word-to-pdf.html')

def w2p_download(request):
    return render(request,'download-page-w2p.html')

def pdf_reader(request):
    return render(request, 'pdf-reader.html')
