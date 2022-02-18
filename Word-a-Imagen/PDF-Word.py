import win32com.client
from PyPDF2 import PdfFileMerger
from shlex import split
from turtle import title
from docx2pdf import convert
from tkinter import Tk, dialog     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import os
import shutil
from pdf2image import convert_from_path
rutaActual = os.getcwd
Tk().withdraw() # elimina la ventana raiz de tkinter

#muestra un cuadro de dialogo explorar y devuelve la ruta del archivo seleccionado
nombreArchivo = askopenfilename(title="Abrir archivo",initialdir =rutaActual)

word = win32com.client.Dispatch("Word.Application")
word.visible = 1
# set the visible to 0, if you dont want to see the word application
print("Ruta del archivo", nombreArchivo)
wordObj = word.Documents.Open(nombreArchivo)
wordObj.SaveAs("doctor1.docx", FileFormat=16)
# File format 16 refers to word file