import os
DIRECTORIO_BASE = os.path.dirname(__file__)
#print(DIRECTORIO_BASE)

#la función .getcwd() obtiene el directorio actual de trabajo del archivo
DIRECTORIO_BASE_2 = os.getcwd()
#print(DIRECTORIO_BASE_2)

#devolver el directorio base o de trabajo pero en formato unicode.
DIRECTORIO_BASE_3 = os.getcwdb()
#print(DIRECTORIO_BASE_3)

# Crear carpeta
#os.mkdir('api')
# Crear carpetas con subcarpetas
#os.makedirs('test2/api')

print(os.listdir(os.path.join(os.getcwd(),'test')))

#Eliminar carpeta
#os.rmdir('api2')

#Eliminar carpetas
#os.removedirs('test2/api')

#import shutil
#shutil.rmtree('diseños') #elimina carpetas, subcarpetas y archivos.

#eliminar archivos
#os.remove(‘Nombre de archivo’)
