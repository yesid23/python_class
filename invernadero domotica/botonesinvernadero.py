#importar librerias para GUi
import serial
from tkinter import *
import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.title("INVERNADERO")
root.resizable(FALSE, FALSE)
root.configure(background="#9C977F")

boton1=Button(root,text="LUZ",width=10,height=5,command=lambda:on_offLuces('1')).place(x=35,y=50)
boton2=Button(root,text="PUERTA",width=10,height=5,command=lambda:on_offLuces('2')).place(x=170,y=50)
boton3=Button(root,text="RIEGO",width=10,height=5,command=lambda:on_offLuces('3')).place(x=170,y=180)
boton4=Button(root,text="VENTILADOR",width=10,height=5,command=lambda:on_offLuces('4')).place(x=35,y=180)




