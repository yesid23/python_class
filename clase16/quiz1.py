#daniel obando - yesid nasner


import serial

#importar librerias para GUI
from tkinter import *
import tkinter

arduino = serial.Serial("COM3", 9600)

root = tkinter.Tk()
root.geometry("400x400")
root.title("Mi calculadora")
root.resizable(FALSE, FALSE)
root.configure(background="#F06041")
######################################
#funciones
def btnCLIK(valor):
    global operador
    operador=operador+str(valor)
    input_text.set(operador)
def clear():
    global operador
    operador=("")
    input_text.set(operador)
def operacion():
    global operador
    try:
        opera=str(eval(operador))#sirvepararealizarlaoperacion
        arduinoData.write(b'+'opera'+')
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)#muestraderusultado
##############################
input_text=StringVar()
operador=""

Display=Entry(root,font=('italy',20,'bold'),width=20,bd=1,insertwidth=2,bg="#E2F041",justify="right",textvariable=input_text).place(x=10,y=60)

boton1=Button(root,text="1",width=7,height=3,command=lambda:btnCLIK(1)).place(x=10,y=100)
boton2=Button(root,text="2",width=7,height=3,command=lambda:btnCLIK(2)).place(x=75,y=100)
boton3=Button(root,text="3",width=7,height=3,command=lambda:btnCLIK(3)).place(x=140,y=100)
boton4=Button(root,text="4",width=7,height=3,command=lambda:btnCLIK(4)).place(x=10,y=160)
boton5=Button(root,text="5",width=7,height=3,command=lambda:btnCLIK(5)).place(x=75,y=160)
boton6=Button(root,text="6",width=7,height=3,command=lambda:btnCLIK(6)).place(x=140,y=160)
boton7=Button(root,text="7",width=7,height=3,command=lambda:btnCLIK(7)).place(x=10,y=220)
boton8=Button(root,text="9",width=7,height=3,command=lambda:btnCLIK(8)).place(x=140,y=220)
boton9=Button(root,text="8",width=7,height=3,command=lambda:btnCLIK(9)).place(x=75,y=220)
boton0=Button(root,text="0",width=7,height=3,command=lambda:btnCLIK(0)).place(x=75,y=285)
botonClear=Button(root,text="clear",width=7,height=3,command=lambda:clear()).place(x=10,y=285)
botonIgual=Button(root,text="=",width=7,height=3,command=operacion).place(x=140,y=285)
botonmas=Button(root,text="+",width=7,height=3,command=lambda:btnCLIK("+")).place(x=224,y=100)
botonmenos=Button(root,text="-",width=7,height=3,command=lambda:btnCLIK("-")).place(x=224,y=160)
botonmultiplicacion=Button(root,text="*",width=7,height=3,command=lambda:btnCLIK("*")).place(x=224,y=220)
botondivicion=Button(root,text="/",width=7,height=3,command=lambda:btnCLIK("/")).place(x=224,y=285)
