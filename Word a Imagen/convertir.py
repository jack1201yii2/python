import aspose.words as aw
import os

# load document
doc = aw.Document("test/api/16511 Iniciativa empresarial joven II.docx")


# set output image format
options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)

# loop through pages and convert them to PNG images
for pageNumber in range(doc.page_count):
    options.page_set = aw.saving.PageSet(pageNumber)
    doc.save("test/api/"+str(pageNumber+1)+"_pag.png", options)
