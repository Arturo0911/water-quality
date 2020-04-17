import random
import numbers
from decimal import *

ListaComponentesIBackup2 = []
ListaComponentesI = ["Antimonio, Sb","Arsénico, As","Bario, Ba","Boro, B","Cadmio, Cd","Cianuros, CN",
                     "Cloro libre residual* ","Cobre, Cu","Cromo, Cr","Fluoruros","Manganeso, Mn","Mercurio, Hg",
                     "Níquel, Ni","Nitratos, NO3","Nitritos, NO2","Plomo, Pb","Selenio, Se"] #COMPONENTES INORGÁNICOS
ListaComponentesIBackup =[]


for i in range (4):
    a = ListaComponentesI[random.randint(0,12)]
    #print(a)
    ListaComponentesI.remove(a)
    ListaComponentesIBackup.append(a)




ListaComponentesO = ["Benzo [a]pireno", "Benceno", "Tolueno", "Xileno", "Estireno", "1,2dicloroetano", "Cloruro de vinilo", "Tricloroeteno",
                     "Tetracloroeteno", "Di(2-etilhexil) ftalato", "Acrylamida", "Epiclorohidrina", "Hexaclorobutadieno", "1,2Dibromoetano ",
                     "1,4- Dioxano", "Acido Nitrilotriacético"] #COMPONENTES ORGÁNICOS

for j in range (4):
    b = ListaComponentesO[random.randint(0,10)]
    ListaComponentesO.remove(b)
    ListaComponentesIBackup2.append(b)


"""

valor1 = int (input("ingrese un numero menor o igual que 4: "))
valor2 = int (input("ingrese un numero menor o igual que 2: "))

if (valor1 > 4) and (valor2 > 2):
    print("ambos numeros son incorrectos")
elif (valor1 <= 4) and (valor2 <= 2):
    print("WIN")
elif (valor1 > 4) and (valor2 <= 2):
    print("primer numero incorrecto")
    print("segundo numero correcto")
elif (valor1 <= 4) and (valor2 > 2):
    print("primer numero correcto")
    print("segundo numero incorrecto")
"""


#valor2 = int (input("ingrese un numero menor o igual que 2: "))
#valor1 = float







"""
while True:
    valor = input("ingrese un numero menor o igual que 2: ")
    num = str(valor)
    if (num.isdecimal()):
        print("Eureka", type(valor))
        break
    else:
        print("LO INGRESADO NO Es numero")
"""

while True:
    try:
        numero = float (input(": "))
        print("OK")
        print(numero)
        break
    except:
        print("ESTE NUMERO NO ES FLOTANTE")




Turbiedad = [3,4,5,6,7,8]
cuvi = Turbiedad[random.randint(0,5)]

print(cuvi)









"""

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
#import CALIDAD_AGUA
import Main_app


Ventana_ingreso = tk.ThemedTk()
Ventana_ingreso.get_themes()     #-------------Returns a list of all themes that can be set
Ventana_ingreso.set_theme("plastik")   #---------------------------Sets an available theme
Ventana_ingreso.geometry("290x300")
Ventana_ingreso.title("LOGIN")
Ventana_ingreso.iconbitmap (r'descarga_gMJ_icon.ico ')
Ventana_ingreso.resizable(False,False)
w = Canvas(Ventana_ingreso, width=200, height=100)
w.pack()


#text = Label(Ventana_ingreso, font =('arial', 16, 'bold'),
             #text="Login", relief="raised",fg="gray1", bd = 10)
#text.pack()


#imagenFondo= PhotoImage(master=w,file = "Aguita.png")
#LabelFondo = ttk.Label(Ventana_ingreso, image = imagenFondo).place(x=0, y=0)



#statusbar = ttk.Label(Ventana_ingreso, text="BIENVENIDOS AGRARIOS", relief=SUNKEN, anchor=W, font='Times 10 italic')
#statusbar.pack(side=BOTTOM, fill=X)



Frame1 = Frame(Ventana_ingreso)   #FRAME IZQUIERDO
Frame1.pack(side = LEFT, padx=30, pady=10)

#Frame2 = Frame(Ventana_ingreso)   #FRAME SUPERIOR
#Frame2.pack(side = TOP, padx=30, pady=10)



#===============================================================================
# FUNCION PARA INGRESAR EL USUARIO Y CONTRASEÑA :v
#===============================================================================


#def ValidarIngreso():
    #if (USUARIO1.get() == 'ADMIN') and (PASSWORD1.get() == '1234'):
        #objeto = Main_app
        #objetoFuncion = objeto.Main()
        #return objetoFuncion
    #else:
        #messagebox.showwarning('ERROR', 'INCORRECT PASSWORD')



#==============================================================================
#==============================================================================


USUARIO = ttk.Label(Frame1, text="USER")
USUARIO.grid(row =0, column=0)


USUARIO1=ttk.Entry(Frame1)
USUARIO1.grid(row=0, column=1)


PASSWORD = ttk.Label(Frame1, text="PASS")
PASSWORD.grid(row=1, column=0)


PASSWORD1=ttk.Entry(Frame1, show="*")
PASSWORD1.grid(row =1, column=1)


#==============================================================================
#==============================================================================



VALIDATE = ttk.Button(Frame1, text= "LOG")
VALIDATE.grid(row = 3, padx=10)



def on_closing():
    Ventana_ingreso.destroy()

Ventana_ingreso.protocol("WM_DELETE_WINDOW", on_closing)
Ventana_ingreso.mainloop()
#def Destruir ():
    #Ventana_ingreso.destroy()


#===============================================================================
#===============================================================================



print(ListaComponentesIBackup)
print(ListaComponentesIBackup2)
print("ASI QUEDA LA LISTA")
print (ListaComponentesI)
print(ListaComponentesO)

"""

"""INORGANICOS = {
    "Antimonio, Sb": 0.02, "Arsénico, As": 0.01, "Bario, Ba": 0.7, "Boro, B": 0.5,
    "Cadmio, Cd": 0.003, "Cianuros, CN": 0.07, "Cloro libre residual* ": 0.3,
    "Cobre, Cu": 2.0, "Cromo, Cr": 0.05, "Fluoruros": 1.5, "Manganeso, Mn": 0.4,
    "Mercurio, Hg": 0.006, "Níquel, Ni": 0.07, "Nitratos, NO3": 50,
    "Nitritos, NO2": 0.2, "Plomo, Pb": 0.01, "Selenio, Se": 0.01

}
print(ListaComponentesIBackup)
print(INORGANICOS)
print(INORGANICOS[ListaComponentesIBackup[0]])

"""




#for k in INORGANICOS:
    #print(k, ":",INORGANICOS[k])

