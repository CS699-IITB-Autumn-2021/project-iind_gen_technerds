from docx2pdf import convert
def d2p(word_path,pdf_path):
	"""
	This Function convert the given docx file into the pdf file

	Paramters
	---------
	word_path(string):path of the word file to be converted to pdf file.
	pdf_path(string): path to which converted pdf file is stored.

	Returns
	-------
	Nothing,word file is directly converted.
	"""
	
	convert(word_path,pdf_path)

#d2p('p2w.docx','w2p.pdf')
