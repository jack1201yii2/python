from shlex import split
from turtle import title
from docx2pdf import convert
from tkinter import Tk, dialog     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import os
rutaActual = os.getcwd
Tk().withdraw() # elimina la ventana raiz de tkinter
#filename = askopenfilename() #muestra un cuadro de dialogo explorar y devuelve la ruta del archivo seleccionado

# try:
rutaNombreArchivo = askopenfilename(title="Abrir archivosaas",initialdir =rutaActual)
s = rutaNombreArchivo.split("/")
nombreArchivo=s[len(s)-1].replace(".docx","")
ruta = "/".join(s[0:-1])
rutaWord= ruta+"/"+nombreArchivo+".docx"
rutaPdf = ruta+"/"+nombreArchivo+".pdf"
convert(rutaWord,rutaPdf)

# except Exception as e:
#     showerror(title="Error",message="Ocurrio un error inesperado: "+str(e))





#convert(r"16511 Iniciativa empresarial joven II.docx",r"16511 Iniciativa empresarial joven II.pdf")