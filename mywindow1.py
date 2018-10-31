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
#funciones

def btnClik(valor):
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
       opera=str(eval(operador))
    except:
       clear()
       opera=("error")
    input.text.set(opera)



#################################
input_text=StringVar()
operador=" "


display=Entry(root,font=('arial',20,'bold'),width=22,bd=1,insertwidth=2,bg="#0BF1EA",justify="right",textvariable=input_text).place(x=25,y=30)

boton1=Button(root,text="1",width=7,height=3,command=lambda:btnClik(1)).place(x=20,y=100)
boton2=Button(root,text="2",width=7,height=3,command=lambda:btnClik(2)).place(x=100,y=100)
boton3=Button(root,text="3",width=7,height=3,command=lambda:btnClik(3)).place(x=180,y=100)
boton4=Button(root,text="4",width=7,height=3,command=lambda:btnClik(4)).place(x=20,y=180)
boton5=Button(root,text="5",width=7,height=3,command=lambda:btnClik(5)).place(x=100,y=180)
boton6=Button(root,text="6",width=7,height=3,command=lambda:btnClik(6)).place(x=180,y=180)
boton7=Button(root,text="7",width=7,height=3,command=lambda:btnClik(7)).place(x=20,y=260)
boton8=Button(root,text="8",width=7,height=3,command=lambda:btnClik(8)).place(x=100,y=260)
boton9=Button(root,text="9",width=7,height=3,command=lambda:btnClik(9)).place(x=180,y=260)
boton0=Button(root,text="0",width=7,height=3,command=lambda:btnClik(0)).place(x=100,y=340)

botonClear=Button(root,text="CLEAR",width=7,height=3,command=lambda:btnClik("=")).place(x=20,y=340)
botonIgual=Button(root,text="=",width=7,height=3,command=lambda:Clear()).place(x=180,y=340)

botonsum=Button(root,text="+",width=7,height=3,command=lambda:btnClik("+")).place(x=280,y=100)
botonres=Button(root,text="-",width=7,height=3,command=lambda:btnClik("-")).place(x=280,y=180)
botonmul=Button(root,text="*",width=7,height=3,command=lambda:btnClik("*")).place(x=280,y=260)
botondiv=Button(root,text="/",width=7,height=3,command=lambda:btnClik("/")).place(x=280,y=340)



#abrir ventana
root.mainloop()
