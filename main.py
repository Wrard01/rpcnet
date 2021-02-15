"""Programa que buasca si el archivo rpcnet se encuentra dentro de los archivos de sistema de windows
   el programa busca en los directorios system32 para la version 64bit y el directorio SysWow64
   para la version de 32 bits, cualquiera de estas versiones podria estar instalada en windows 64 bits"""
import tkinter
import os

"""Funcion que busca el archivo en el folder System32"""


def s64():
    lbl2.config(text='File not found in System32', fg='black')
    basepath = 'C://Windows//System32//'
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.name == "rpcnet.exe":
                lbl2.config(text=entry.name + ' File found  in System32', fg='red')


"""Funcion que busca el archivo en el folder SysWow64"""


def s32():
    lbl2.config(text='File not found in SysWow64', fg="black")
    basepath1 = 'C://Windows//SysWow64//'
    with os.scandir(basepath1) as entries:
        for entry in entries:
            if entry.name == "rpcnet.exe":
                lbl2.config(text=entry.name + ' File found in SysWow64', fg='red')


"""Funcin que regresa el texto a pantalla inicial"""


def cls():
    lbl2.config(text='Click on a button to Search', fg='black')


"""Creacion de los elementos de la inteface"""
top = tkinter.Tk()
top.title("rpcnet Finder By Mel")
lbl = tkinter.Label(top, text="Search for rpcnet.exe ")
lbl.config(font=("Trebuchet ms", 30))
nuevo = tkinter.Button(top, text=" System32 ", command=s64)
nuevo.config(font=("Trebuchet ms", 20))
viejo = tkinter.Button(top, text=" SysWow64 ", command=s32)
viejo.config(font=("Trebuchet ms", 20))
clear = tkinter.Button(top, text="  Reset  ", command=cls)
clear.config(font=("Trebuchet ms", 20))
lbl2 = tkinter.Label(top, text="Click on a button to Search")
lbl2.config(font=("Trebuchet ms", 20))

"""Colocacion de los elementos de la interface"""
lbl.place(x=150, y=35)
nuevo.place(x=110, y=130)
viejo.place(x=320, y=130)
clear.place(x=540, y=130)
lbl2.place(x=110, y=230)


top.geometry("750x330")
top.resizable(False, False)
top.mainloop()
