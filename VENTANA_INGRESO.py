import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk
import CALIDAD_AGUA
#import Main_app


Ventana_ingreso = tk.ThemedTk()
Ventana_ingreso.get_themes()
Ventana_ingreso.set_theme('plastik')
Ventana_ingreso.resizable(False, False)
w = Canvas(Ventana_ingreso, width=200, height=100)
w.pack()

imagenFondo= PhotoImage(master=w,file = "Aguita.png")
LabelFondo = Label(Ventana_ingreso, image = imagenFondo).place(x=0, y=0)

loginImagen = PhotoImage(master=w,file = "icon.png")
claveImagen = PhotoImage(master=w,file = "clave.png")



Loginfoto = PhotoImage (master=w,file = "LOGIN.png")
LabelFondo2 = Label(Ventana_ingreso, image = Loginfoto).place(x=110, y=50)



statusbar = ttk.Label(Ventana_ingreso, text="BIENVENIDOS AGRARIOS", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.pack(side=BOTTOM, fill=X)



#Frame1 = Frame(Ventana_ingreso)   #FRAME IZQUIERDO    icon.png
#Frame1.pack(side = LEFT, padx=30, pady=10)

#Frame2 = Frame(Ventana_ingreso)   #FRAME SUPERIOR
#Frame2.pack(side = TOP, padx=30, pady=10)




Ventana_ingreso.geometry("290x270")
Ventana_ingreso.title("LOGIN")
Ventana_ingreso.iconbitmap (r'descarga_gMJ_icon.ico ')

#===============================================================================
# FUNCION PARA INGRESAR EL USUARIO Y CONTRASEÑA :v    LOGIN.png
#===============================================================================

c = 0
def ValidarIngreso():


    if (USUARIO1.get() == 'ADMIN') and (PASSWORD1.get() == '1234'):
        Ventana_ingreso.destroy()
        objetoCalidad = CALIDAD_AGUA
        objetoagua = objetoCalidad.openwindow()
        return objetoagua


    else:
        messagebox.showwarning('ERROR', 'INCORRECT PASSWORD')

def Destroy ():
    ValidarIngreso()
    Ventana_ingreso.destroy()


#==============================================================================
#==============================================================================

#text = ttk.Label(Frame2,text="Login")
#text.grid(row=0, column=1)

#LogginLabel = Label(Frame1,image = Loginfoto)
#LogginLabel.grid(row =0, column=0)

USUARIO = ttk.Label(Ventana_ingreso, text="USER")
USUARIO.place(x=50, y =150)
#USUARIO.grid(row =1, column=0)


USUARIO1=ttk.Entry(Ventana_ingreso)
USUARIO1.place(x=100, y =150)
#USUARIO1.grid(row=1, column=1)


PASSWORD = ttk.Label(Ventana_ingreso, text="PASS")
#PASSWORD.grid(row=2, column=0)
PASSWORD.place(x=50, y = 180)

PASSWORD1=ttk.Entry(Ventana_ingreso, show="*")
#PASSWORD1.grid(row =2, column=1)
PASSWORD1.place(x=100, y =180)

#==============================================================================
#==============================================================================


VALIDATE = ttk.Button(Ventana_ingreso, text= "LOG", command = ValidarIngreso)
#VALIDATE.grid(row = 3, padx=10)
VALIDATE.place(x=115, y =220)

#===============================================================================
#===============================================================================

Ventana_ingreso.mainloop()