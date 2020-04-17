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

#imagenFondo= PhotoImage(master=w,file = "Aguita.png")
#LabelFondo = Label(Ventana_ingreso, image = imagenFondo).place(x=0, y=0)


Loginfoto = PhotoImage (master=w,file = "LOGIN.png")
LabelFondo2 = Label(Ventana_ingreso, image = Loginfoto).place(x=110, y=50)



statusbar = ttk.Label(Ventana_ingreso, text="BIENVENIDOS AGRARIOS", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.pack(side=BOTTOM, fill=X)



Frame1 = Frame(Ventana_ingreso)   #FRAME IZQUIERDO
Frame1.pack(side = LEFT, padx=30, pady=10)

Frame2 = Frame(Ventana_ingreso)   #FRAME SUPERIOR
Frame2.pack(side = TOP, padx=30, pady=10)




Ventana_ingreso.geometry("290x250")
Ventana_ingreso.title("LOGIN")
Ventana_ingreso.iconbitmap (r'descarga_gMJ_icon.ico ')

#===============================================================================
# FUNCION PARA INGRESAR EL USUARIO Y CONTRASEÑA :v    LOGIN.png
#===============================================================================


def ValidarIngreso():
    if (USUARIO1.get() == 'ADMIN') and (PASSWORD1.get() == '1234'):
        objetoCalidad = CALIDAD_AGUA
        objetoagua = objetoCalidad.openwindow()
        return objetoagua
    else:
        messagebox.showwarning('ERROR', 'INCORRECT PASSWORD')


#==============================================================================
#==============================================================================

#text = ttk.Label(Frame2,text="Login")
#text.grid(row=0, column=1)

#LogginLabel = Label(Frame1,image = Loginfoto)
#LogginLabel.grid(row =0, column=0)

USUARIO = ttk.Label(Frame1, text="USER")
USUARIO.grid(row =1, column=0)


USUARIO1=ttk.Entry(Frame1)
USUARIO1.grid(row=1, column=1)


PASSWORD = ttk.Label(Frame1, text="PASS")
PASSWORD.grid(row=2, column=0)


PASSWORD1=ttk.Entry(Frame1, show="*")
PASSWORD1.grid(row =2, column=1)


#==============================================================================
#==============================================================================


VALIDATE = ttk.Button(Frame1, text= "LOG", command = ValidarIngreso)
VALIDATE.grid(row = 3, padx=10)

#===============================================================================
#===============================================================================

Ventana_ingreso.mainloop()