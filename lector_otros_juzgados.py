##datos proxy 
##tacuari-iws1.jusbaires.gob.ar
##puerto 8080

from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from PIL import ImageTk, Image
import os
import pyperclip as pc

root = Tk()
root.config(width=1280, height=720)
root.resizable(0,0)
root.title("Utilidad DNIs")
style = ttk.Style(root)
root.configure(bg='#DCDAD5')
print(style.theme_names())



def getFilePath(filePath):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = filePath
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path

#Creo widget tipo label
def get_input():

    try:
        value=my_text_box.get("1.0","end-1c")
        if not value:
            raise ValueError
        value = value.replace('@','"' )
        valueList = value.split('"')
        #Posiciones array, 0 - Numero de tramite, 1 + 2 Apellido y FUCK
        #Okay so como hago ahora para darle otra forma?
        #Hago otro array o que? Hm. :thinking:
        #Nomas tengo que hacer dos variaciones, mismo orden final, Nombre, DNI, Fecha de nacimiento, Sexo DNI.
        dniONumDeTramite = valueList[0]

        if len(dniONumDeTramite) >= 10:
            #en este caso es DNI de 2012-Actualidad

            try:
                teststr = "Apellido y Nombre: " + valueList[1] + " " + valueList[2] + ", DNI: " + valueList[4] + ", Fecha de nacimiento: " + valueList[6] + ", el sexo que figura en el DNI: " + valueList[3]
            except ValueError:
                print(ValueError)
        else:
            #en este caso es DNI de 2009-2012 
            try: 
                teststr = "Apellido y Nombre: " + valueList[4] + " " + valueList[5] + ", DNI: " + valueList[1].replace(' ', '') + ", Fecha de nacimiento: " + valueList[7] + ", el sexo que figura en el DNI: " + valueList[8]
                            
            except ValueError: 
                print(ValueError)
        
        

        global valueFormatted
        valueFormatted = str(teststr)

        valueList = []

        my_text_box.delete("1.0", END)
        my_text_box.insert("1.0", teststr)
        print(value)
        pc.copy(valueFormatted)
        my_text_box.configure(state='disabled')

    except IndexError:
        messagebox.showwarning("Ojo", "Ya lo formateaste esto! \n Proba borrando el texto.")
    except ValueError:
        messagebox.showwarning("Ojo", "Esta vacio")

def deleteTextBox():
    my_text_box.configure(state='normal')    
    my_text_box.delete("1.0", END)

def openTextBox():
    filepath2 = filedialog.askopenfilename(
        filetypes=[("Archivos .txt","*.txt"),("Todos los archivos", "*.*")]
    )
    if not filepath2:
        return
    with open(filepath2, "r") as input_file:
        global openedText
        openedText = input_file.read()
        root.title(f"Utilidad DNIs - {filepath2}")

def saveTextBox():
    global filePath1
    filePath1 = filedialog.asksaveasfilename(defaultextension='txt',
    filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if not filePath1:
        return
    with open(filePath1, "a") as output_file:

        try:
            textFileThingy = openedText + "\n" + valueFormatted + "\n"
            output_file.write(textFileThingy)
        except NameError:
            textFileThingy = valueFormatted + "\n"
            output_file.write(textFileThingy)            
            root.title(f"Utilidad DNIs - {filePath1}")


image2 = Image.open(getFilePath('logo-cmcaba.png'))
resize_image2_scale = .7
image2_x = 444
image2_y = 71
resize_image2 = image2.resize ((int(image2_x*resize_image2_scale), int(image2_y*resize_image2_scale)))
img2 = ImageTk.PhotoImage(image=resize_image2)
imgLabel2 = Label(root, image= img2)
imgLabel2.image = img2


creditsLabel = Label(root, text="Por Ilan Fritzler, JPCyF 10", font=('Calibri',10))
myLabel2 = Label(root, text="Como usar la utilidad \n 1. Escanear (Se copia automaticamente al portapapeles) \n 2. Guardar \n 3. Borrar \n 4. Repetir todas las veces necesarias \n Si necesitamos guardar en un archivo .txt que ya existe, usamos antes de todo Abrir .txt", font=("Calibri", 12), justify=LEFT)
openButton = Button(root, text= "Abrir .txt", command=openTextBox)
saveButton = Button(root, text="Guardar .txt", command=saveTextBox)
myLabel = Label(root, text="Convertir Texto de Lector a Algo Legible", font=("Calibri", 12))
myButton = Button(root, text="Convertir", command=get_input)
deleteButton = Button(root, text="Borrar Texto", command=deleteTextBox)
#Creating a text box widget
my_text_box=Text(root, height=15, width=90, font=("Calibri", 12))

#Lo muestro
imgLabel2.pack(anchor=E,padx=95)
myLabel2.pack(anchor=W, padx=130)
my_text_box.pack()
myLabel.pack()
openButton.pack(side=LEFT,padx=170)
saveButton.pack(side=RIGHT,padx=170)
myButton.pack()
deleteButton.pack()
creditsLabel.pack()
style.theme_use('clam')
root.mainloop()