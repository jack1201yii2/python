from pdf2image import convert_from_path
ruta = "C:/Users/Usuario/Documents/Python/Word a Imagen/test/16511 Iniciativa empresarial joven II.pdf"
images = convert_from_path(ruta, 500,poppler_path=r"C:\Program Files\poppler-22.01.0\Library\bin")
for i in range(len(images)):
	# Save pages as images in the pdf
	images[i].save('C:/Users/Usuario/Documents/Python/Word a Imagen/test/pagina'+ str(i) +'.jpg', 'JPEG')