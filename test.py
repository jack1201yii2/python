import win32com.client
word = win32com.client.Dispatch("Word.Application")
word.visible = 1
ruta = "C:/Users/Usuario/Desktop/RVOE"
wordObj = word.Documents.Open(ruta+".pdf")
wordObj.SaveAs(ruta+".docx", FileFormat=16)