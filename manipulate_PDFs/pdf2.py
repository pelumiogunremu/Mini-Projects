import PyPDF2
import sys

pdf_list = sys.argv[1:]

def pdfs_merger(input):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merger.append(pdf)

	merger.write('super.pdf')

pdfs_merger(pdf_list)

