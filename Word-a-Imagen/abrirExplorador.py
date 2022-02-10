#############Version 1###################
# import  tkinter as tk
# from tkinter import filedialog
# root = tk.Tk()
# root.withdraw() # elimina la ventana raiz de tkinter
# file_path = filedialog.askopenfilename()
# print(file_path)


#############Version 2###################
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename, askopenfilenames

Tk().withdraw() # elimina la ventana raiz de tkinter
filenames = askopenfilenames() #muestra un cuadro de dialogo explorar y devuelve la ruta del archivo seleccionado
for filename in filenames:
    print(filename)