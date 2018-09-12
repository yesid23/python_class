#cajero automatico
print("cajero automatico")
atras = ("y")
intentos = 3
saldo = 1.000.000
while intentos >= 0:
	clave = int(input("digite su clave:"))
	
	if clave == (1234): 
	    print("clave correcto ")

	while atras not in ("n", "no", "N", "No"):
	   print("====menu===/n1-saldo/n2-retiro/n3-cambiarclave/n4-salir/n====")

	    op = int(input())

	    if op == 1:
		    print("su saldo actual es:" saldo)
		    atras input("desea realizae otra operacion?[y/n]")
		    if atras in ("n", "no", "N", "No"):
			 print("")
			 print("gracias...")
			 exit()

	    elif op == 2:
		 retiro = int(input("/[10.000/n 20.000/n 50.000/n 100.000/n 200.000/n 400.000/n 600.000/n 1.000.000/n]:  dijite la cantidad a retirar : "))

		 if retiro in [10.000, 20.000, 50.000, 100.000, 200.000, 400.000, 600.000, 1.000.000,]: 
			saldo = retiro
			print("su saldo es ", saldo)
			atras = input("desea realizae otra operacion?[y/n]")

		    if atras in ("n", "no", "N", "No"):
			print("")
			print("gracias...")
			exit()

		 elif retiro = [10.000, 20.000, 50.000, 100.000, 200.000, 400.000, 600.000, 1.000.000,]: 
			print("cantidad no valida")
			atras = input("desea realizae otra operacion?[y/n]")
		    if atras in ("n", "no", "N", "No"):
			print("gracias...")
			exit()

		elif retiro == 1:
			retiro = int(input("intenta otra cantidad"))

	    elif op == 3:
		 cambiarclave= int(input("digite la cantidad a cambiar:"))
		 clave = cambiarclave
		 print("su nueva clave es", clave)

		 if atras in ("n", "no", "N", "No"):
			print("")
			print("gracias...")
			exit()

	    elif op==4:
		print("cerrando....")
		exit()
elif clave = ('1234'):
	print("clave incorrecto")
	intentos = 1

if intentos == 0:
		print("no mas intentos, gracias por usar el cajero de **UNCENTAVOMAS**")
		break
