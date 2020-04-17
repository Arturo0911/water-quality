import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import os
import threading
import time
import pandas as pd
from pandas.io.excel import ExcelWriter
from pandas.io.common import _stringify_path
from openpyxl.workbook import Workbook
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk
import random
from datetime import datetime, date, time, timedelta
import calendar
from matplotlib import pyplot
day = date.today()
#import VENTANA_INGRESO
import FUNCIONES_AGUA



#==================================================================FUNCION PARA HACER EL LOGGIN




def openwindow():
    root = tk.ThemedTk()
    root.get_themes()  # Returns a list of all themes that can be set
    root.set_theme("radiance")  # Sets an available theme
    w = Canvas(root, width=200, height=100)
    w.pack()
    messagebox.showinfo('WELCOME', 'Bienvenidos a nuestro Software que nos permite medir la calidad del agua, '
                                   'utilizando un modelo matemático, en los siguientes parametros estan especificados los botones que nos permiten'
                                   ' calcular todo lo que ingresemos de forma manual, cabe recalcar que la turbiedad del agua estamos usando valores '
                                   'aleatorios para que con cada prueba que se haga se corrobore si esta con un nivel de turbiedad optimo o no.')
    #imagenFondo = PhotoImage(master=w, file="AGUOTA.png")
    #LabelFondo = Label(root, image=imagenFondo).place(x=0, y=0)

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

    def Informacion2():
        def func():
            l2.configure(text=cb.get())
            if (cb.get() == "Inorgánicos"):
                Nroot = tk.ThemedTk()
                Nroot.get_themes()  # Returns a list of all themes that can be set
                Nroot.set_theme("plastik")  # Sets an available # theme
                # w = Canvas(Nroot, width=100, height=100)
                # w.pack()

                statusbar = ttk.Label(Nroot, text="BIENVENIDOS AGRARIOS", relief=SUNKEN, anchor=W,
                                      font='Times 10 italic')
                statusbar.pack(side=BOTTOM, fill=X)
                menubar = Menu(Nroot)
                Nroot.config(menu=menubar)
                subMenu = Menu(menubar, tearoff=0)

                # menubar.add_cascade(label="File", menu=subMenu)
                # subMenu.add_command(label="Exit", command=root.destroy)

                Nroot.geometry("350x150")
                Nroot.title("UNIVERSIDAD AGRARIA DEL ECUADOR")
                Nroot.iconbitmap(r'descarga_gMJ_icon.ico ')
                leftframe = Frame(Nroot)
                leftframe.pack(side=LEFT, padx=30, pady=30)

                Label1 = ttk.Label(leftframe, text=" Valores inorgánicos ")
                Label1.grid(row=0, column=0, padx=10)

                none1 = ttk.Label(leftframe, text="")
                none1.grid(row=0, column=1, padx=10)

                medida = ttk.Label(leftframe, text="mg/l")
                medida.grid(row=0, column=2, padx=10)

                none2 = ttk.Label(leftframe, text="")
                none2.grid(row=0, column=3, padx=10)

                resultado = ttk.Label(leftframe, text="3.29")
                resultado.grid(row=0, column=4, padx=10)

                # ======================================================================================================

                agua = ttk.Label(leftframe, text=" Turbiedad del agua")
                agua.grid(row=1, column=0, padx=10)

                none3 = ttk.Label(leftframe, text="")
                none3.grid(row=1, column=1, padx=10)

                medida2 = ttk.Label(leftframe, text="Pt-Cu")
                medida2.grid(row=1, column=2, padx=10)

                none4 = ttk.Label(leftframe, text="")
                none4.grid(row=1, column=3, padx=10)

                resultado2 = ttk.Label(leftframe, text="5")
                resultado2.grid(row=1, column=4, padx=10)

                Nroot.mainloop()

        # Frame2 = Frame(win)   #FRAME SUPERIOR
        # Frame2.pack(side = TOP, padx=30, pady=10)
        win = Toplevel()
        win.geometry('150x150')
        course = ["Orgánicos", "Inorgánicos"]

        l1 = ttk.Label(win, text="Tabla de VAlores")
        l1.grid(column=3, row=0)
        cb = ttk.Combobox(win, values=course, width=10)
        cb.grid(column=3, row=1)
        cb.current(0)
        b = Button(win, text="Click Here", command=func)
        b.grid(column=3, row=2)
        l2 = ttk.Label(win, text="")
        l2.grid(column=3, row=3)
        win.mainloop()

    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Open", command=Informacion2)
    subMenu.add_command(label="Exit", command=root.destroy)



    def about_us():
        tkinter.messagebox.showinfo('Calidad del agua', 'Aqui emplemamos el modelo matemático'
                                                        ' comprendido por la formula f(x,y,z) donde'
                                                        ' los parámetros principales son:'
                                                        ' los compuestos inorgánicos deben tener un valor limite máximo de '
                                                        '3.29 mg/l dejando fuera la radiación total ya que no está en la misma medida'
                                                        '. Sustancias orgánicas 0,47 mg/l ')

    def presentarIntegrantes():
        ven = Toplevel()
        ven.title("INTEGRANTES")
        ven.resizable(False, False)
        tex = "\n MARGARITA CORREA TOLEDO\n JUAN FRANCISCO CUVI FEIJOO \n EVELYN DEL ROCIO CARDENAS TRELLES\n DENISSE YAMILEX VERA VERA\n"
        l1 = Label(ven, text=tex, height=0, width=50)
        l1.pack()

    def Informacion():

        Nroot = tk.ThemedTk()
        Nroot.get_themes()  # Returns a list of all themes that can be set
        Nroot.set_theme("plastik")  # Sets an available # theme
        # w = Canvas(Nroot, width=100, height=100)
        # w.pack()

        statusbar = ttk.Label(Nroot, text="BIENVENIDOS AGRARIOS", relief=SUNKEN, anchor=W, font='Times 10 italic')
        statusbar.pack(side=BOTTOM, fill=X)
        menubar = Menu(Nroot)
        Nroot.config(menu=menubar)
        subMenu = Menu(menubar, tearoff=0)

        # menubar.add_cascade(label="File", menu=subMenu)
        # subMenu.add_command(label="Exit", command=root.destroy)

        Nroot.geometry("350x150")
        Nroot.title("UNIVERSIDAD AGRARIA DEL ECUADOR")
        Nroot.iconbitmap(r'descarga_gMJ_icon.ico ')
        leftframe = Frame(Nroot)
        leftframe.pack(side=LEFT, padx=30, pady=30)

        Label1 = ttk.Label(leftframe, text=" Valores inorgánicos ")
        Label1.grid(row=0, column=0, padx=10)

        none1 = ttk.Label(leftframe, text="")
        none1.grid(row=0, column=1, padx=10)

        medida = ttk.Label(leftframe, text="3.29")
        medida.grid(row=0, column=2, padx=10)

        none2 = ttk.Label(leftframe, text="")
        none2.grid(row=0, column=3, padx=10)

        resultado = ttk.Label(leftframe, text="mg/l")
        resultado.grid(row=0, column=4, padx=10)

        #==============================================================================================================

        org = ttk.Label(leftframe, text=" Valores orgánicos ")
        org.grid(row=1, column=0, padx=10)

        none5 = ttk.Label(leftframe, text="")
        none5.grid(row=1, column=1, padx=10)

        medida = ttk.Label(leftframe, text="0.47")
        medida.grid(row=1, column=2, padx=10)

        none6 = ttk.Label(leftframe, text="")
        none6.grid(row=1, column=3, padx=10)

        resultado3 = ttk.Label(leftframe, text="mg/l")
        resultado3.grid(row=1, column=4, padx=10)

        # ======================================================================================================

        agua = ttk.Label(leftframe, text=" Turbiedad del agua")
        agua.grid(row=2, column=0, padx=10)

        none3 = ttk.Label(leftframe, text="")
        none3.grid(row=2, column=1, padx=10)

        medida2 = ttk.Label(leftframe, text="5")
        medida2.grid(row=2, column=2, padx=10)

        none4 = ttk.Label(leftframe, text="")
        none4.grid(row=2, column=3, padx=10)

        resultado2 = ttk.Label(leftframe, text="Pt-Cu")
        resultado2.grid(row=2, column=4, padx=10)

        # ======================================================================================================

        # ======================================================================================================

        Nroot.mainloop()


    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)

    subMenu.add_command(label="About Us", command=about_us)
    subMenu.add_command(label="Desarrolladores", command=presentarIntegrantes)
    #subMenu.add_command(label="Informacion", command=Informacion)


    root.geometry("1100x600")
    root.title("UNIVERSIDAD AGRARIA DEL ECUADOR")
    root.iconbitmap(r'descarga_gMJ_icon.ico ')
    root.resizable(False,False)

    text = Label(root, font=('arial', 16, 'bold'),
                 text="SISTEMA DE MEDICION DE CALIDAD DEL AGUA", relief="raised", fg="gray1", bd=10)
    text.pack()

    # ===========================================================================================

    # =============================FUNCIONES=====================================================





    # =========================================================================================== BUSCAR.png

    photo = PhotoImage(master=w,file ='START.png')
    photo2 = PhotoImage(master=w,file='EXCEL.png')
    photo3 = PhotoImage(master=w,file='DELETE.png')
    photo4 = PhotoImage(master=w,file='Power.png')
    photo5 = PhotoImage(master=w,file='graficas.png')
    photo6 = PhotoImage(master=w, file='BUSCAR.png')

    # =============================================LISTAS CON PARAMETROS RANDOM==============================================

    ListaComponentesIBackup = []  # COMPONENTES INORGÁNICOS
    ListaComponentesIBackup2 = []  # COMPONENTES ORGÁNICOS

    VALUES = {  # ===========================================VALORES INORGANICAS
        "Antimonio, Sb": 0.02, "Arsénico, As": 0.01, "Bario, Ba": 0.7, "Boro, B": 0.5,
        "Cadmio, Cd": 0.003, "Cianuros, CN": 0.07, "Cloro libre residual* ": 0.3,
        "Cobre, Cu": 2.0, "Cromo, Cr": 0.05, "Fluoruros": 1.5, "Manganeso, Mn": 0.4,
        "Mercurio, Hg": 0.006, "Níquel, Ni": 0.07, "Nitratos, NO3": 50,
        "Nitritos, NO2": 0.2, "Plomo, Pb": 0.01, "Selenio, Se": 0.01
    }

    VALUES2 = {  # ===========================================VALORES ORGANICAS
        "Benzo [a]pireno": 0.0007, "Benceno": 0.01, "Tolueno": 0.7, "Xileno": 0.5,
        "Estireno": 0.02, "1,2dicloroetano": 0.03, "Cloruro de vinilo": 0.0003,
        "Tricloroeteno": 0.02, "Tetracloroeteno": 0.04, "Di(2-etilhexil) ftalato": 0.008, "Acrylamida": 0.0005,
        "Epiclorohidrina": 0.0004, "Hexaclorobutadieno": 0.0006, "1,2Dibromoetano": 0.0004,
        "1,4- Dioxano": 0.05, "Acido Nitrilotriacético": 0.2, "Isoproturón": 0.009, "Lindano": 0.002,
        "Pendimetalina": 0.02, "Pentaclorofenol": 0.009,
        "Dicloroprop": 0.1, "Alacloro": 0.02, "Aldicarb": 0.01, "Aldrín y Dieldrín ": 0.00003, "Carbofuran": 0.007,
        "Clorpirifós": 0.03,
        "DDT y metabolitos": 0.01, "1,2-Dibromo-3-cloropropano": 0.001, "1,3-Dicloropropeno": 0.02,
        "Dimetoato": 0.006,
        "Endrín": 0.0006, "Terbutilazina": 0.007, "Clordano": 0.0002
    }


    ListaComponentesI = ["Antimonio, Sb", "Arsénico, As", "Bario, Ba", "Boro, B", "Cadmio, Cd", "Cianuros, CN",
                         "Cloro libre residual* ", "Cobre, Cu", "Cromo, Cr", "Fluoruros", "Manganeso, Mn",
                         "Mercurio, Hg",
                         "Níquel, Ni", "Nitratos, NO3", "Nitritos, NO2", "Plomo, Pb",
                         "Selenio, Se"]  # COMPONENTES INORGÁNICOS

    for i in range(4):
        a = ListaComponentesI[random.randint(0, 12)]
        ListaComponentesI.remove(a)
        ListaComponentesIBackup.append(a)

    ListaComponentesO = ["Benzo [a]pireno", "Benceno", "Tolueno", "Xileno", "Estireno", "1,2dicloroetano",
                         "Cloruro de vinilo", "Tricloroeteno",
                         "Tetracloroeteno", "Di(2-etilhexil) ftalato", "Acrylamida", "Epiclorohidrina",
                         "Hexaclorobutadieno", "1,2Dibromoetano ",
                         "1,4- Dioxano", "Acido Nitrilotriacético", "Isoproturón", "Lindano", "Pendimetalina",
                         "Pentaclorofenol", "Dicloroprop",
                         "Alacloro", "Aldicarb", "Aldrín y Dieldrín ", "Carbofuran", "Clorpirifós", "DDT y metabolitos",
                         "1,2-Dibromo-3-cloropropano",
                         "1,3-Dicloropropeno", "Dimetoato", "Endrín", "Terbutilazina",
                         "Clordano"]  # COMPONENTES ORGÁNICOS

    for j in range(4):
        b = ListaComponentesO[random.randint(0, 10)]
        ListaComponentesO.remove(b)
        ListaComponentesIBackup2.append(b)

    Transparencia = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  # UNIDADES DE MEDIDA    ...... Pt-Co
    Turbiedad = [3, 4, 5, 6, 7, 8]  # UNIDADES DE MEDIDA  .....NTU
    ListapH_agua = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                    15]  # VALORES DEL pH DEL AGUA QUE A MEDIDA DE QUE AUMENTA EL pH DEL AGUA AUMENTA EL COLOR

    # FUNCIONES==================================================================================



    def Calculo_de_valores_organicos_inorganicos():

        SumaInorganica = 0

        INORGANICOS = {  # ===========================================VALORES INORGANICAS
            "Antimonio, Sb": 0.02, "Arsénico, As": 0.01, "Bario, Ba": 0.7, "Boro, B": 0.5,
            "Cadmio, Cd": 0.003, "Cianuros, CN": 0.07, "Cloro libre residual* ": 0.3,
            "Cobre, Cu": 2.0, "Cromo, Cr": 0.05, "Fluoruros": 1.5, "Manganeso, Mn": 0.4,
            "Mercurio, Hg": 0.006, "Níquel, Ni": 0.07, "Nitratos, NO3": 50,
            "Nitritos, NO2": 0.2, "Plomo, Pb": 0.01, "Selenio, Se": 0.01
        }

        while not False:
            try:
                EI1 = float(EntVariable1.get())  # PRIMERA ENTRADA DE LOS COMPONENTES INORGANICOS

                EI2 = float(EntVariable2.get())  # SEGUNDA ENTRADA DE LOS COMPONENTES INORGANICOS

                EI3 = float(EntVariable3.get())  # TERCERA ENTRADA DE LOS COMPONENTES INORGANICOS

                EI4 = float(EntVariable4.get())  # CUARTA ENTRADA DE LOS COMPONENTES INORGANICOS


                if (EI1 <= INORGANICOS[ListaComponentesIBackup[0]]):
                    SumaInorganica = SumaInorganica + EI1

                    if (EI2 <= INORGANICOS[ListaComponentesIBackup[1]]):
                        SumaInorganica = SumaInorganica + EI2

                        if (EI3 <= INORGANICOS[ListaComponentesIBackup[2]]):
                            SumaInorganica = SumaInorganica + EI3

                            if (EI4 <= INORGANICOS[ListaComponentesIBackup[3]]):
                                SumaInorganica = SumaInorganica + EI4
                                if (SumaInorganica <= 3.29):
                                    Suma = (str(SumaInorganica) + "mg/l")

                                    messagebox.showinfo('VALUE', Suma)
                                    d = int(
                                        ((float(EntVariable1.get()) / (INORGANICOS[ListaComponentesIBackup[0]])) * 25))
                                    f = int(
                                        ((float(EntVariable2.get()) / (INORGANICOS[ListaComponentesIBackup[1]])) * 25))
                                    c = int(
                                        ((float(EntVariable3.get()) / (INORGANICOS[ListaComponentesIBackup[2]])) * 25))
                                    r = int(
                                        ((float(EntVariable4.get()) / (INORGANICOS[ListaComponentesIBackup[3]])) * 25))
                                    graficar = [d, f, c, r]
                                    labels = ListaComponentesIBackup[0], ListaComponentesIBackup[1], \
                                             ListaComponentesIBackup[2], ListaComponentesIBackup[3]

                                    explode = (0, 0.1, 0, 0)
                                    col = ('#0da0c1', '#e39106', '#25b413', '#b6e2ec')
                                    _, _, arturo = pyplot.pie(graficar, explode=explode, labels=labels, colors=col,
                                                              autopct='%1.1f%%')

                                    for tex in arturo:
                                        tex.set_color('white')
                                    pyplot.axis('equal')
                                    pyplot.title('Grafica de datos')
                                    pyplot.show()
                                else:
                                    messagebox.showwarning('CAUTION ',
                                                           'El valor de la suma ' + str(
                                                               SumaInorganica) + 'mg/l excede el limite permitido')
                                    EntVariable1.delete(0, END)
                                    EntVariable2.delete(0, END)
                                    EntVariable3.delete(0, END)
                                    EntVariable4.delete(0, END)

                            else:
                                messagebox.showwarning('CAUTION ',
                                                       'El valor' + ListaComponentesIBackup[
                                                           3] + ' excede el limite permitido')
                                EntVariable4.delete(0, END)
                        else:
                            messagebox.showwarning('CAUTION ',
                                                   'El valor' + ListaComponentesIBackup[
                                                       2] + ' excede el limite permitido')
                            EntVariable3.delete(0, END)

                    else:
                        messagebox.showwarning('CAUTION ',
                                               'El valor' + ListaComponentesIBackup[1] + ' excede el limite permitido')
                        EntVariable2.delete(0, END)
                else:
                    messagebox.showwarning('CAUTION ',
                                           'El valor' + ListaComponentesIBackup[0] + ' excede el limite permitido')
                    EntVariable1.delete(0, END)
                break
            except:
                messagebox.showerror('ERROR', 'OTRA VEZ :v')
                EntVariable1.delete(0, END)
                EntVariable2.delete(0, END)
                EntVariable3.delete(0, END)
                EntVariable4.delete(0, END)
                break


        # =============================================================================================================================================

    def Calculo_de_valores_organicos_organicos():
        SumaOrganica = 0

        ORGANICOS = {  # ===========================================VALORES ORGANICAS
            "Benzo [a]pireno": 0.0007, "Benceno": 0.01, "Tolueno": 0.7, "Xileno": 0.5,
            "Estireno": 0.02, "1,2dicloroetano": 0.03, "Cloruro de vinilo": 0.0003,
            "Tricloroeteno": 0.02, "Tetracloroeteno": 0.04, "Di(2-etilhexil) ftalato": 0.008, "Acrylamida": 0.0005,
            "Epiclorohidrina": 0.0004, "Hexaclorobutadieno": 0.0006, "1,2Dibromoetano": 0.0004,
            "1,4- Dioxano": 0.05, "Acido Nitrilotriacético": 0.2, "Isoproturón": 0.009, "Lindano": 0.002,
            "Pendimetalina": 0.02, "Pentaclorofenol": 0.009,
            "Dicloroprop": 0.1, "Alacloro": 0.02, "Aldicarb": 0.01, "Aldrín y Dieldrín ": 0.00003, "Carbofuran": 0.007,
            "Clorpirifós": 0.03,
            "DDT y metabolitos": 0.01, "1,2-Dibromo-3-cloropropano": 0.001, "1,3-Dicloropropeno": 0.02,
            "Dimetoato": 0.006,
            "Endrín": 0.0006, "Terbutilazina": 0.007, "Clordano": 0.0002
        }

        while not False:
            try:
                EI5 = float(EntVariable5.get())  # PRIMERA ENTRADA DE LOS COMPONENTES ORGANICOS

                EI6 = float(EntVariable6.get())  # SEGUNDA ENTRADA DE LOS COMPONENTES ORGANICOS

                EI7 = float(EntVariable7.get())  # TERCERA ENTRADA DE LOS COMPONENTES ORGANICOS

                EI8 = float(EntVariable8.get())  # CUARTA ENTRADA DE LOS COMPONENTES ORGANICOS
                messagebox.showinfo('CONTINUE', '.........')

                if (EI5 <= ORGANICOS[ListaComponentesIBackup2[0]]):
                    SumaOrganica = SumaOrganica + EI5

                    if (EI6 <= ORGANICOS[ListaComponentesIBackup2[1]]):
                        SumaOrganica = SumaOrganica + EI6

                        if (EI7 <= ORGANICOS[ListaComponentesIBackup2[2]]):
                            SumaOrganica = SumaOrganica + EI7

                            if (EI8 <= ORGANICOS[ListaComponentesIBackup2[3]]):
                                SumaOrganica = SumaOrganica + EI8
                                if (SumaOrganica <= 0.47):
                                    Suma2 = (str(SumaOrganica) + "mg/l")
                                    messagebox.showinfo('VALUE', Suma2)

                                    ar = int(((EI5 / (ORGANICOS[ListaComponentesIBackup2[0]])) * 25))
                                    ju = int(((EI6 / (ORGANICOS[ListaComponentesIBackup2[1]])) * 25))
                                    jf = int(((EI7 / (ORGANICOS[ListaComponentesIBackup2[2]])) * 25))
                                    ev = int(((EI8 / (ORGANICOS[ListaComponentesIBackup2[3]])) * 25))
                                    graficar = [ar, ju, jf, ev]
                                    labels = ListaComponentesIBackup2[0], ListaComponentesIBackup2[1], \
                                             ListaComponentesIBackup2[2], ListaComponentesIBackup2[3]

                                    explode = (0, 0.1, 0, 0)
                                    col = ('#0da0c1', '#e39106', '#25b413', '#b6e2ec')
                                    _, _, arturo = pyplot.pie(graficar, explode=explode, labels=labels, colors=col,
                                                              autopct='%1.1f%%')

                                    for tex in arturo:
                                        tex.set_color('white')
                                    pyplot.axis('equal')
                                    pyplot.title('Grafica de datos')
                                    pyplot.show()
                                else:
                                    messagebox.showwarning('CAUTION ',
                                                           'El valor de la suma ' + str(
                                                               SumaOrganica) + 'mg/l excede el limite permitido')
                            else:
                                messagebox.showwarning('CAUTION ',
                                                       'El valor' + ListaComponentesIBackup2[
                                                           3] + ' excede el limite permitido')
                                EntVariable8.delete(0, END)
                        else:
                            messagebox.showwarning('CAUTION ',
                                                   'El valor' + ListaComponentesIBackup2[
                                                       2] + ' excede el limite permitido')
                            EntVariable7.delete(0, END)

                    else:
                        messagebox.showwarning('CAUTION ',
                                               'El valor' + ListaComponentesIBackup2[1] + ' excede el limite permitido')
                        EntVariable6.delete(0, END)
                else:
                    messagebox.showwarning('CAUTION ',
                                           'El valor' + ListaComponentesIBackup2[0] + ' excede el limite permitido')
                    EntVariable5.delete(0, END)
                break
            except:
                messagebox.showerror('ERROR', 'Se deben ingresar valores de tipo numérico')
                EntVariable5.delete(0, END)
                EntVariable6.delete(0, END)
                EntVariable7.delete(0, END)
                EntVariable8.delete(0, END)
                break

        # ============================================================================================

    def Save_file():
        nobjeto = str
        nobjeto2 = str
        #listaobjeto = Calculo_de_valores_organicos_inorganicos(nobjeto)
        #listaobjeto2 = Calculo_de_valores_organicos_organicos(nobjeto2)

        #NlistaInorganica

        LISTA_SAVE_NOMBRES_INORGANICOS = [
            ListaComponentesIBackup[0], ListaComponentesIBackup[1],
            ListaComponentesIBackup[2], ListaComponentesIBackup[3]
        ]

        LISTA_SAVE_INORGANICA = [
            float(EntVariable1.get()), float(EntVariable2.get()),
            float(EntVariable3.get()), float(EntVariable4.get())
            ]

        #======================================================================================================================

        LISTA_SAVE_NOMBRES_ORGANICOS = [
            ListaComponentesIBackup2[0], ListaComponentesIBackup2[1],
            ListaComponentesIBackup2[2], ListaComponentesIBackup2[3]
        ]

        LISTA_SAVE_ORGANICA = [
            float(EntVariable5.get()), float(EntVariable6.get()),
            float(EntVariable7.get()), float(EntVariable8.get())
            ]

        #CREAREMOS 4 COLUMNAS PARA COLOCAR LOS VALORES DE ENTRADAS ORGÁNICAS E INORGÁNICAS  ENTRADAEXCEL

        nombre = str (ENTRADAEXCEL.get())
        df = pd.DataFrame()


        df['ELEMENTOS INORGÁNICOS'] = LISTA_SAVE_NOMBRES_INORGANICOS[0::2]
        df['VALORES INORGÁNICOS'] = LISTA_SAVE_INORGANICA[1::2]
        df['ELEMENTOS INORGÁNICOS'] = LISTA_SAVE_NOMBRES_ORGANICOS[2::2]
        df['VALORES INORGÁNICOS'] = LISTA_SAVE_ORGANICA[3::2]

        df.to_excel(nombre +'.xlsx', index=False)  # CONVERTIMOS A EXCEL



    #============================================================================================================

    def Graficar():
        d = int(((float(EntVariable1.get()) / (VALUES[ListaComponentesIBackup[0]])) * 25))
        f = int(((float(EntVariable2.get()) / (VALUES[ListaComponentesIBackup[1]])) * 25))
        c = int(((float(EntVariable3.get()) / (VALUES[ListaComponentesIBackup[2]])) * 25))
        r = int(((float(EntVariable4.get()) / (VALUES[ListaComponentesIBackup[3]])) * 25))
        ar = int(((float(EntVariable5.get()) / (VALUES2[ListaComponentesIBackup2[0]])) * 25))
        ju = int(((float(EntVariable6.get()) / (VALUES2[ListaComponentesIBackup2[1]])) * 25))
        jf = int(((float(EntVariable7.get()) / (VALUES2[ListaComponentesIBackup2[2]])) * 25))
        ev = int(((float(EntVariable8.get()) / (VALUES2[ListaComponentesIBackup2[3]])) * 25))
        nuevadata = [d, f, c, r, ar, ju, jf, ev]
        explode = (0, 0.1, 0, 0, 0, 0, 0, 0)
        labels = ListaComponentesIBackup[0], ListaComponentesIBackup[1], ListaComponentesIBackup[2], \
                 ListaComponentesIBackup[3], ListaComponentesIBackup2[0], ListaComponentesIBackup2[1], \
                 ListaComponentesIBackup2[2], ListaComponentesIBackup2[3]
        col = ('#0da0c1', '#e39106', '#25b413', '#b6e2ec', '#a0c10d', '#011013', '#310303', '252323')
        _, _, arturo = pyplot.pie(nuevadata, explode=explode, labels=labels, colors=col, autopct='%1.1f%%')
        for tex in arturo:
            tex.set_color('white')
        pyplot.axis('equal')
        pyplot.title('Grafica de datos')
        pyplot.show()

    def Valores():
        ven = tk.ThemedTk()
        ven.get_themes()  # Returns a list of all themes that can be set
        ven.set_theme("plastik")  # Sets an available theme
        ven.title("VALORES RECOMENDADOS")
        ven.geometry("900x500")
        ven.resizable(False, False)
        root.iconbitmap(r'descarga_gMJ_icon.ico ')

        newframe = Frame(ven)  # FRAME IZQUIERDO
        newframe.pack(side=LEFT, padx=30, pady=10)

        tex = "HOLI"
        l1 = ttk.Label(newframe, text=tex)
        l1.grid(row=0, column=0)

        l1 = ttk.Label(newframe)
        l1.grid(row=0, column=1)

        l1 = ttk.Label(newframe, text=tex)
        l1.grid(row=0, column=2)

        l1 = ttk.Label(newframe)
        l1.grid(row=0, column=3)

        l1 = ttk.Label(newframe, text=tex)
        l1.grid(row=0, column=4)
        ven.mainloop()



    def VerificarVAlores():

        EntradaRandom = ttk.Entry(middleframe)
        EntradaRandom.grid(row=3, column=1)



        cuvi = Turbiedad[random.randint(0, 5)]
        EntradaRandom.insert(0, cuvi)
        while not False:
            try:

                EI1 = float(EntVariable1.get())  # PRIMERA ENTRADA DE LOS COMPONENTES INORGANICOS

                EI2 = float(EntVariable2.get())  # SEGUNDA ENTRADA DE LOS COMPONENTES INORGANICOS

                EI3 = float(EntVariable3.get())  # TERCERA ENTRADA DE LOS COMPONENTES INORGANICOS

                EI4 = float(EntVariable4.get())  # CUARTA ENTRADA DE LOS COMPONENTES INORGANICOS

                EI5 = float(EntVariable5.get())  # PRIMERA ENTRADA DE LOS COMPONENTES ORGANICOS

                EI6 = float(EntVariable6.get())  # SEGUNDA ENTRADA DE LOS COMPONENTES ORGANICOS

                EI7 = float(EntVariable7.get())  # TERCERA ENTRADA DE LOS COMPONENTES ORGANICOS

                EI8 = float(EntVariable8.get())  # CUARTA ENTRADA DE LOS COMPONENTES ORGANICOS

                Total1 = EI1 + EI2 + EI3 + EI4
                Total2 = EI5 + EI6 + EI7 + EI8

                if (Total1 > 3.29) and (Total2 > 0.47) and (cuvi > 5):
                    messagebox.showwarning('CAUTION ', 'Los valores orgánicos, inorgánicos y turbiedad del agua'
                                                       ' excenden el limite permitido en la calidad del agua')


                elif (Total1 <= 3.29) and (Total2 <= 0.47) and (cuvi <= 5):
                    messagebox.showinfo('VALUES',
                                        'El sistema corrobora que la calidad del agua está con los parametros correctos')
                    BotonExcel = ttk.Button(middleframe, image=photo2, command=Save_file)
                    BotonExcel.grid(row=1, column=0, padx=10)
                    GraficasButton = ttk.Button(middleframe, image=photo6, command=Graficar)
                    GraficasButton.grid(row=0, column=1, padx=10)


                elif (Total1 <= 3.29) and (Total2 <= 0.47) and (cuvi > 5):
                    messagebox.showwarning('CAUTION',
                                           'Los valores orgánicos e inorgánicos se encuentran optimos pero el nivel de turbiedad del'
                                           ' agua no permite una calidad adecuada')


                elif (Total1 <= 3.29) and (Total2 > 0.47):
                    messagebox.showwarning('CAUTION',
                                           'Los valores orgánicos son los idóneos pero los valores inorgánicos se encuentran fuera del rango'
                                           ' permitido')


                elif (Total1 > 3.29) and (Total2 <= 0.47):
                    messagebox.showwarning('CAUTION',
                                           'Los valores inorgánicos son los idóneos pero los valores orgánicos se encuentran fuera del rango'
                                           ' permitido')
                break

            except:
                messagebox.showwarning('CAUTION ', 'No se puede ejecutar el programa si no hay valores de entrada')
                break



    # ===========================================ETIQUETAS INORGANICAS

    # ========================================== FRAMES ==================================================

    leftframe = Frame(root)
    leftframe.pack(side=LEFT, padx=30, pady=30)

    rightframe = Frame(root)
    rightframe.pack(pady=30)

    topframe = Frame(rightframe)
    topframe.pack()

    #lengthlabel = ttk.Label(topframe, text='Medidor Arduino')
    #lengthlabel.pack(pady=5)

    currenttimelabel = ttk.Label(topframe, text=day, relief=GROOVE)
    currenttimelabel.pack()

    middleframe = Frame(rightframe)
    middleframe.pack(pady=30, padx=30)

    # ===========================================ETIQUETAS INORGANICAS

    LabelInorganico = ttk.Label(leftframe, text="VALORES INORGÁNICOS")
    LabelInorganico.grid(row=0, column=0)

    LabelImaginario1 = ttk.Label(leftframe)  # LABEL IMAGINARIO
    LabelImaginario1.grid(row=1, column=0)

    IngVariable1 = ttk.Label(leftframe, text=ListaComponentesIBackup[0])
    IngVariable1.grid(row=2, column=0)

    IngVariable2 = ttk.Label(leftframe, text=ListaComponentesIBackup[1])
    IngVariable2.grid(row=3, column=0)

    IngVariable3 = ttk.Label(leftframe, text=ListaComponentesIBackup[2])
    IngVariable3.grid(row=4, column=0)

    IngVariable4 = ttk.Label(leftframe, text=ListaComponentesIBackup[3])
    IngVariable4.grid(row=5, column=0)

    LabelImaginario2 = ttk.Label(leftframe)  # LABEL IMAGINARIO
    LabelImaginario2.grid(row=6, column=0)

    BotonInicio = ttk.Button(leftframe, image=photo, command=Calculo_de_valores_organicos_inorganicos)
    BotonInicio.grid(row=7, column=0, padx=10)

    # ===========================================ETIQUETAS ORGANICAS

    Labelorganico = ttk.Label(leftframe, text="VALORES INORGÁNICOS")
    Labelorganico.grid(row=0, column=2)

    LabelImaginario3 = ttk.Label(leftframe)  # LABEL IMAGINARIO
    LabelImaginario3.grid(row=1, column=2)

    IngVariable5 = ttk.Label(leftframe, text=ListaComponentesIBackup2[0])
    IngVariable5.grid(row=2, column=2)

    IngVariable6 = ttk.Label(leftframe, text=ListaComponentesIBackup2[1])
    IngVariable6.grid(row=3, column=2)

    IngVariable7 = ttk.Label(leftframe, text=ListaComponentesIBackup2[2])
    IngVariable7.grid(row=4, column=2)

    IngVariable8 = ttk.Label(leftframe, text=ListaComponentesIBackup2[3])
    IngVariable8.grid(row=5, column=2)

    LabelImaginario4 = ttk.Label(leftframe)  # LABEL IMAGINARIO
    LabelImaginario4.grid(row=6, column=2)

    BotonInicio = ttk.Button(leftframe, image=photo, command=Calculo_de_valores_organicos_organicos)
    BotonInicio.grid(row=7, column=2, padx=10)

    # ============================================================================================

    # ===========================================ENTRADAS INORGANICAS

    EntVariable1 = ttk.Entry(leftframe)
    EntVariable1.grid(row=2, column=1)

    EntVariable2 = ttk.Entry(leftframe)
    EntVariable2.grid(row=3, column=1)

    EntVariable3 = ttk.Entry(leftframe)
    EntVariable3.grid(row=4, column=1)

    EntVariable4 = ttk.Entry(leftframe)
    EntVariable4.grid(row=5, column=1)

    # ===========================================ENTRADAS ORGANICAS

    EntVariable5 = ttk.Entry(leftframe)
    EntVariable5.grid(row=2, column=3)

    EntVariable6 = ttk.Entry(leftframe)
    EntVariable6.grid(row=3, column=3)

    EntVariable7 = ttk.Entry(leftframe)
    EntVariable7.grid(row=4, column=3)

    EntVariable8 = ttk.Entry(leftframe)
    EntVariable8.grid(row=5, column=3)

    # ============================================================================================

    BotonInicio = ttk.Button(middleframe, image=photo4, command=VerificarVAlores)
    BotonInicio.grid(row=0, column=0, padx=10)

    GraficasButton1 = ttk.Button(middleframe, image=photo5, command=Informacion)
    GraficasButton1.grid(row=1, column=1, padx=10)

    LabelRAndom1 = ttk.Label(middleframe)  # LABEL IMAGINARIO
    LabelRAndom1.grid(row=2, column=0)

    labelrandom = ttk.Label(middleframe, text="TURBIEDAD")
    labelrandom.grid(row=3, column=0)

    LabelRAndom2 = ttk.Label(middleframe)  # LABEL IMAGINARIO
    LabelRAndom2.grid(row=2, column=1)

    labelexcel = ttk.Label(middleframe, text="GUARDAR COMO")
    labelexcel.grid(row=4, column=0)

    ENTRADAEXCEL = ttk.Entry(middleframe)
    ENTRADAEXCEL.grid(row=4, column=1)





    # ============================================================================================
    def on_closing():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()




