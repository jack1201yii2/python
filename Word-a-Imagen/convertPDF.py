from dataclasses import replace
from PyPDF2 import PdfFileMerger
from docx2pdf import convert
from tkinter import Tk    # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import *
import os
rutaActual = os.getcwd
Tk().withdraw() # elimina la ventana raiz de tkinter

#muestra un cuadro de dialogo explorar y devuelve la ruta del archivo seleccionado
nombreArchivos = askopenfilenames(title="Abrir archivos",initialdir =rutaActual)
nombreArchivosPDFs = []
ruta = ""
for rutaNombreArchivo in nombreArchivos:
    s = rutaNombreArchivo.split("/")
    nombreArchivo=s[len(s)-1].replace(".docx","").strip() #obtenemos el nombre del archivo y quitamos los espacios
    ruta = "/".join(s[0:-1])
    print(nombreArchivo)
    rutaArchivo= ruta+"/"+nombreArchivo
    convert(rutaArchivo+".docx",rutaArchivo+".pdf")
    nombreArchivosPDFs.append(rutaArchivo+".pdf")

#Unir PDF's
nombre_archivo_salida = "salida.pdf"
fusionador = PdfFileMerger()

for rutaNombreArchivoPDF in nombreArchivosPDFs:
    fusionador.append(open(rutaNombreArchivoPDF, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    #print("Ruta PDF"+str(ruta)+"/"+str(salida.name))
    fusionador.write(str(ruta)+"/"+str(salida.name))