#ejercicio menu calculadora
import os # importar librerias del sistema

os.system("cls")
print("menu pricipal")
print("1. suamar numeros")
print("2. restar numeros")
print("3. multiplicar numeros")
print("4. dividir numeros")
print(".:::dijite su opcion:")
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero numero: "))
opc=int(input("dijite la operacion a realizar: "))
if opc == 1 :
 suma = num1 + num2
 print("la suma es: ", suma)
 
elif opc == 2:
 resta = num1 - num2
 print("la resta es: ", resta)
 
elif opc == 3 :
 multiplicacion = num1 * num2
 print("la multiplicacion es: ", multiplicacion)
 
 
elif opc == 4 :
 division = num1 / num2
 print("la division es: ", division)
 
 
 
 
