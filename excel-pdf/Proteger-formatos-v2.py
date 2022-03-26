# Import Module
from turtle import title
from win32com import client
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import os
from tkinter import Tk    # from tkinter import Tk for Python 3.x
from tkinter.messagebox import *
from docx2pdf import convert
from pdf2image import convert_from_path
from PIL import Image #para guardar imagen a pdf
import shutil

rutaActual = os.getcwd
Tk().withdraw()
def convertirImagenPDF(ruta,nombreArchivo,rutaImagenes):
    imagensN = []#almacenamos la imgen abierta mediante la ruta
    imsN = [] #guardamos la imagen convertida
    cont = 0
    for rutaImagen in rutaImagenes:
        imagensN.append(Image.open(rutaImagen))
        imsN.append(imagensN[cont].convert('RGB'))
        cont+=1
    imsN[0].save(ruta+nombreArchivo+'.pdf', save_all=True, append_images=imsN[0:-1])
    shutil.rmtree(ruta+nombreArchivo)
    showinfo(title='Mensaje', message='La protecion del archivo \"'+nombreArchivo+'\", se ha realizado de forma exitosa.')
    os.startfile(ruta)
def convertirPdfImagen(ruta, nombreArchivo, bandera=0):
    if bandera==1:
        images = convert_from_path(ruta+nombreArchivo.replace(' ','%20')+".pdf", 500,poppler_path=r"C:\Program Files\poppler-22.01.0\Library\bin")
    else:    
        images = convert_from_path(ruta+nombreArchivo+".pdf", 500,poppler_path=r"C:\Program Files\poppler-22.01.0\Library\bin")
    rutaImagenes = []
    for i in range(len(images)):
        # guardamos las paginas del pdf como imagenes
        rutaImagenes.append(ruta+nombreArchivo+'/pagina'+ str(i+1)+'.jpg')
        images[i].save(ruta+nombreArchivo+'/pagina'+ str(i+1) +'.jpg', 'JPEG')
    if bandera==1:
        os.remove(ruta+nombreArchivo.replace(' ','%20')+".pdf")
    else:
        os.remove(ruta+nombreArchivo+".pdf")
    convertirImagenPDF(ruta,nombreArchivo,rutaImagenes)

def convertirExcelPdf(ruta, nombreArchivo):
    #Creamos un objeto de tipo COM (Excel)
    excel = client.Dispatch("Excel.Application")
    #Abrimos la ruta del excel
    sheets = excel.Workbooks.Open(ruta+nombreArchivo+'.xlsx')
    work_sheets = sheets.Worksheets[0]
    
    # Luego lo convertiremos a PDF usando el método ExportAsFixedFormat()
    work_sheets.ExportAsFixedFormat(0,ruta+nombreArchivo+'.pdf')
    convertirPdfImagen(ruta, nombreArchivo, bandera=1)

def convertirWordPDF(ruta, nombreArchivo):
    convert(ruta+nombreArchivo+'.docx',ruta+nombreArchivo+".pdf")
    convertirPdfImagen(ruta, nombreArchivo)

#rutaNombreArchivo = askopenfilename(title="Abrir archivo", filetypes=[('Archivos de excel','*.xlsx'),('Archivos de word','*.docx'),('All files', '*.*')])
rutaNombreArchivo = askopenfilename(title="Abrir archivo", filetypes=[('Archivos de excel y word','*.xlsx .docx')], initialdir =rutaActual)
s = rutaNombreArchivo.split("/")
nombreArchivoExtencion=s[-1]
ruta = '/'.join(s[0:-1])+'/'
#buscamos donde esta el ultimo . y el tamaño de string para obtener la extencion
extencion = nombreArchivoExtencion[nombreArchivoExtencion.rfind('.'):len(nombreArchivoExtencion)]
#quitamos la extencion al nombre del archivo
nombreArchivo=nombreArchivoExtencion.replace(extencion,'')
if os.path.isdir(ruta+nombreArchivo) != False:
    valor=askyesno(title="¡Advertencia!", message="Aparentemente ya has protegido este archivo previamente.\nPosiblemente tenga algun error\nPara evitarlo elimine la carpeta o cambie el nombre\n¿Deseas continuar?")
    if valor == False:
        quit()
else:
    os.mkdir(ruta+nombreArchivo) #crear el direcotorio donde se guardaran las imagnes
if os.path.isfile(ruta+nombreArchivo+'.pdf') != False:
    valor=askyesno(title="¡Advertencia!", message="Aparentemente ya has protegido este archivo previamente.\nPosiblemente tenga algun error\nPara evitarlo elimine el archivo o cambie el nombre\n¿Deseas continuar?")
    print(valor)
    if valor == False:
        quit()
if extencion=='.xlsx':
    convertirExcelPdf(ruta,nombreArchivo)
elif extencion=='.docx':
    convertirWordPDF(ruta,nombreArchivo)
else:
    showerror(title='Error', message='El archivo no es compatible: \nSolo archivos de word con extencion .docx\nSolo archivos de excel con extencion .xlsx')