import tkinter as tk
#import FUNCIONES
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
#import Archivo
#import serial
import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
#import Archivo
from tkinter import ttk
from ttkthemes import themed_tk as tk




Funcion = tk.ThemedTk()
Funcion.get_themes()  # Returns a list of all themes that can be set
Funcion.set_theme("radiance")  # Sets an available theme

def foto ():
    photo = PhotoImage(file='007-chip.png')

def foto2():
    photo2 = PhotoImage(file='001-360-degrees.png')

def foto3():
    photo3 = PhotoImage(file='006-cpu.png')
"""


root = tk.ThemedTk()
root.get_themes()  # Returns a list of all themes that can be set
root.set_theme("radiance")  # Sets an available theme

        # Fonts - Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys,
        # MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana
        #
        # Styles - normal, bold, roman, italic, underline, and overstrike.

statusbar = ttk.Label(root, text="BIENVENIDOS AGRARIOS", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.pack(side=BOTTOM, fill=X)

        # BARRA DE MENU
menubar = Menu(root)
root.config(menu=menubar)

    # Create the submenu
subMenu = Menu(menubar, tearoff=0)
playlist = []



menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo('About Melody',
                                        'This is a music player build using Python Tkinter by @attreyabhatt')

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

        # mixer.init() #inizializacion
root.geometry("500x500")
root.title("UNIVERSIDAD AGRARIA DEL ECUADOR")
root.iconbitmap(r'descarga_gMJ_icon.ico ')

text = Label(root, font=('arial', 16, 'bold'),
                    text="SISTEMA DE MEDICION DE CALIDAD DEL AGUA", relief="raised", fg="gray1", bd=10)
text.pack()

    # ==========================================================================================

photo = PhotoImage(file='007-chip.png')
photo2 = PhotoImage(file='001-360-degrees.png')
photo3 = PhotoImage(file='006-cpu.png')
    # FUNCIONES==================================================================================


            # datos = np.arange(0, 100)
            # plt.plot([1, 2, 3, 4,5,6,7,8,9,10])
            #plt.ylabel('PAREMETERS ARDUINO')
            # print(A1)
            #plt.plot(Registro2)
            #plt.show()

        # ============================================================================================

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30, pady=30)

playlistbox = Listbox(leftframe, width=30)
playlistbox.pack()

        #addBtn = ttk.Button(leftframe, text="+ Add", command=browse_file)
        #addBtn.pack(side=LEFT)
delBtn = ttk.Button(leftframe, text="- Del")
delBtn.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(pady=30)

topframe = Frame(rightframe)
topframe.pack()

lengthlabel = ttk.Label(topframe, text='Medidor Arduino')
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(topframe, text='Graficas de Valores', relief=GROOVE)
currenttimelabel.pack()

middleframe = Frame(rightframe)
middleframe.pack(pady=30, padx=30)


BotonProposito = ttk.Button(middleframe, image=photo2)
BotonProposito.grid(row=0, column=1, padx=10)

BontonIntegrantes = ttk.Button(middleframe, image=photo3)
BontonIntegrantes.grid(row=0, column=2, padx=10)

        # ============================================================================================
def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
#root.mainloop()


"""