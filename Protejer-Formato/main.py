from shlex import split
from turtle import title
from docx2pdf import convert
from tkinter import Tk, dialog     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import *
import os
import shutil
from pdf2image import convert_from_path
from PIL import Image #para guardar imagen a pdf
rutaActual = os.getcwd
Tk().withdraw() # elimina la ventana raiz de tkinter

#muestra un cuadro de dialogo explorar y devuelve la ruta del archivo seleccionado
nombreArchivos = askopenfilenames(title="Abrir archivos",initialdir =rutaActual)
for rutaNombreArchivo in nombreArchivos:
    s = rutaNombreArchivo.split("/")
    nombreArchivo=s[len(s)-1].replace(".docx","").strip() #obtenemos el nombre del archivo y quitamos los espacios
    ruta = "/".join(s[0:-1])
    rutaArchivo= ruta+"/"+nombreArchivo
    #comprovamos si existe la carpeta
    if os.path.isdir(rutaArchivo) != False:
        showwarning(title="¡Advertencia!", message="Aparentemente ya has convertido este archivo a imagenes previamente.")
    else:
        os.mkdir(rutaArchivo) #crear el direcotorio donde se guardaran las imagnes
    #convertimos el archivo de word a pdf
    convert(rutaArchivo+".docx",rutaArchivo+".pdf")
    #convertimos el pdf a word
    images = convert_from_path(rutaArchivo+".pdf", 500,poppler_path=r"C:\Program Files\poppler-22.01.0\Library\bin")
    rutaImagenes = []
    for i in range(len(images)):
        # guardamos las paginas del pdf como imagenes
        rutaImagenes.append(rutaArchivo+'/pagina'+ str(i+1)+'.jpg')
        images[i].save(rutaArchivo+'/pagina'+ str(i+1) +'.jpg', 'JPEG')
    os.remove(rutaArchivo+".pdf")
    imagensN = []#almacenamos la imgen abierta mediante la ruta
    imsN = [] #guardamos la imagen convertida
    cont = 0
    for rutaImagen in rutaImagenes:
        imagensN.append(Image.open(rutaImagen))
        imsN.append(imagensN[cont].convert('RGB'))
        cont+=1
    
    imsN[0].save(rutaArchivo+'.pdf', save_all=True, append_images=imsN[0:-1])
    shutil.rmtree(rutaArchivo)
    #showinfo(title="Mensaje", message="Se han creado: "+str(len(images))+" Imagenes")
