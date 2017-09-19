def ordenamiento_por_insercion(arreglo):
	for indice in range(1,len(arreglo)):
		valor = arreglo[lista]
		i = lista - 1
		while i>=0:
			if valor < arreglo[i]:
				arreglo[i+1] = arreglo[i]
				arreglo[i] = valor
				i = i - 1
			else:
				break

			
 A=[4,1,3,5,22,8,500]
 ordenamiento_por_insercion(A)
 print (A)
