import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list: None):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('.\sample_pdf\super.pdf')


# def pdf_watermaker(srd_pdf_list, wtr_filename):


# pdf_combiner(inputs)

# with open('.\sample_pdf\dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     # print(reader.numPages)
#     page0 = reader.getPage(0)
#     page0.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page0)
#     with open('.\sample_pdf\tile.pdf', 'wb') as new_file:
#         writer.write(new_file)


