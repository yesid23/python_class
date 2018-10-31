#importar librerias para GUI
from tkinter import *
import tkinter

###################################


#crear ventana
root = tkinter.Tk()
root.geometry("400x400")#wxh
root.title(".::MI CALCULADORA::.")
root.resizable(FALSE, FALSE)
root.configure(background="#283747")

#################################
display=Entry(root,font=('arial',20,'bold'),width=22,bd=1,insertwidth=2,bg="#0BF1EA",justify="right").place(x=25,y=60)
boton1=button(root,text="1",width=7,height=3).place(x=10,y=60)



#abrir ventana
 #root.mainlopp()
