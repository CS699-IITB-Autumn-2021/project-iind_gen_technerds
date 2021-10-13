def compressFile(f):
    with open(f.name, 'w') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
