def ordenamiento_por_burbuja(arreglo):
	for i in range(len(arreglo)):
		for valor in range(len(arreglo)-1):
			if arreglo[valor] > arreglo[valor + 1]:
				aux = arreglo[valor]
				arreglo[valor] = arreglo[valor + 1]
				arreglo[valor + 1] = aux

				
A=[4,67,21,23,56,3,4,75,34,96,1]
ordenamiento_por_burbuja(A)
print(A)