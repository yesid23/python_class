#tablas de multiplicar
rango = 1
tabla_mul = int(input("ingrese la tabla que desea realizar: "))
rango_tab = int(input("ingrese el rango de la tabla, hasta donde desea desarrollar: "))
while rango <= rango_tab :
	print (tabla_mul, "*", rango, "=", tabla_mul * rango)
	rango = rango + 1
