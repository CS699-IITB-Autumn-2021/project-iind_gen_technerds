from pylovepdf.ilovepdf import ILovePdf

ilovepdf = ILovePdf('project_public_acea6791941b90040052bcfa605303c5_4zSbs98325f7c19dfbc3987d56ed81421ab8a', verify_ssl=True)
task = ilovepdf.new_task('compress')

task.add_file('report.pdf')
task.set_output_folder('G:/IITB/cs699 - software lab/project')
task.execute()
task.download()
task.delete_current_task()
