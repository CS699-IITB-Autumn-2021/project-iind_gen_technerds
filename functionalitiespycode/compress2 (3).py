from pylovepdf.ilovepdf import ILovePdf
import sys
def compress(inp_file,out_path):
	"""
	This Function Compress the given pdf file

	Paramters
	---------
	inp_file(string):path of the pdf file to be compressed
	out_path(string):output path where compressed file will be stored

	Returns
	-------
	Nothing,compressed file is downloaded directly.
	"""
	#object of ilovepdf api is created
	ilovepdf_object = ILovePdf('project_public_38b3ce7f045cce26af4788599d0b86b7_jwnijcf52e52d6ed850f0e797ebf4c4fea348', verify_ssl=True)
	#compress task of api is called
	task_compress = ilovepdf_object.new_task('compress')

	task_compress.add_file(inp_file)
	task_compress.set_output_folder(out_path)
	#given file will now will compress
	task_compress.execute()
	#compressed file will be downloaded in output folder which is set above
	task_compress.download()
	task_compress.delete_current_task()

#https://github.com/AndyCyberSec/pylovepdf