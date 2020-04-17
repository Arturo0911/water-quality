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

def Main():
    root = tk.ThemedTk()
    root.get_themes()  # Returns a list of all themes that can be set
    root.set_theme("plastik")  # Sets an available # theme
    w = Canvas(root, width=100, height=100)
    w.pack()

    statusbar = ttk.Label(root, text="BIENVENIDOS AGRARIOS", relief=SUNKEN, anchor=W, font='Times 10 italic')
    statusbar.pack(side=BOTTOM, fill=X)
    menubar = Menu(root)
    root.config(menu=menubar)
    subMenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Exit", command=root.destroy)

    def about_us():
        ven = Toplevel()
        ven.title("About us")
        ven.resizable(False, False)
        tex = "\nEste es un programa para medir la calidad del agua \n a partir de un modelo matemático\n"
        Label(ven, text="").pack()
        l1 = Label(ven, text=tex, height=0, width=50)
        l1.pack()
        Label(ven, text="").pack()

    def presentarIntegrantes():
        ven = tk.ThemedTk()
        ven.get_themes()  # Returns a list of all themes that can be set
        ven.set_theme("radiance")  # Sets an available theme
        ven.title("VALORES RECOMENDADOS")
        root.geometry("1100x500")
        ven.resizable(False, False)
        root.iconbitmap(r'descarga_gMJ_icon.ico ')
        tex = "\n JULISSA MARGARITA CORREA TOLEDO\n JUAN FRANCISCO CUVI FEIJOO \n EVELYN DEL ROCIO CARDENAS TRELLES\n DENISSE YAMILEX VERA VERA\n"
        l1 = Label(ven, text=tex, height=0, width=50)
        l1.pack()
        ven.mainloop()



    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)

    subMenu.add_command(label="RESUMEN", command=about_us)
    subMenu.add_command(label="DESARROLADORES", command=presentarIntegrantes)

    root.geometry("200x500")
    root.title("UNIVERSIDAD AGRARIA DEL ECUADOR")
    root.iconbitmap(r'descarga_gMJ_icon.ico ')
    #root.resizable(False, False)

    # =====================================================================
    # =========================FRAMES======================================
    leftframe = Frame(root)
    leftframe.pack(side=TOP, padx=30, pady=30)

    #middleframe = Frame(rightframe)
    #middleframe.pack(pady=30, padx=30)

    #topframe = Frame(rightframe)
    #topframe.pack()

    # =====================================================================
    # FUNCION DE LOS BOTONES PRINCIPALES

    def CalidadAgua(): # AQUI ABRIMOS EL ARCHIVO CALIDAD AGUA
        objetoCalidad = CALIDAD_AGUA
        objetoagua = objetoCalidad.openwindow()
        return objetoagua

    #def AbrirFunciones(): #ABRIMOS EL ARCHIVO DE FUNCIONES DONDE HAYAMOS LOS PARAMETROS DEL AGUA
        #ObjetoFuncion = FUNCIONES_AGUA #VARIABLE QUE CONTIENE LA FUNCION PARA ABRIR EL ARCHIVO FUNCION

        #F_A = ObjetoFuncion


    # =====================================================================



    #Iniciar = ttk.Label(topframe, text = "Start")
    #Iniciar.grid()

    BotonArduino = ttk.Button(leftframe,text = "Inicio", command= CalidadAgua)
    BotonArduino.grid(row=0, column=0, padx=10)

    BotonProposito = ttk.Button(leftframe,text = "Values")
    BotonProposito.grid(row=1, column=0, padx=10)

    BontonIntegrantes = ttk.Button(leftframe,text = "Close")
    BontonIntegrantes.grid(row=2, column=0, padx=10)

    #BotonGraficas = ttk.Button(leftframe, text="Graficas")
    #BotonGraficas.grid(row=3, column=0, padx=10)


    root.mainloop()