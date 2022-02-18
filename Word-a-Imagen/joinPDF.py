from PyPDF2 import PdfFileMerger
from shlex import split
from turtle import title
from docx2pdf import convert
from tkinter import Tk, dialog     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import *
import os
import shutil
from pdf2image import convert_from_path
rutaActual = os.getcwd
Tk().withdraw() # elimina la ventana raiz de tkinter

#muestra un cuadro de dialogo explorar y devuelve la ruta del archivo seleccionado
nombreArchivos = askopenfilenames(title="Abrir archivos",initialdir =rutaActual)
nombre_archivo_salida = "salida.pdf"
fusionador = PdfFileMerger()

for rutaNombreArchivo in nombreArchivos:
    fusionador.append(open(rutaNombreArchivo, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)