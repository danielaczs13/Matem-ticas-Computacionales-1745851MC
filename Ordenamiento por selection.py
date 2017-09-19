def ordenamiento_por_selection(arreglo):
	for i in range(0, len(arreglo) - 1):
		minvalor = i
		for j in range (i+1, len(arreglo)):
			if arreglo[j] < arreglo[minvalor]:
				minvalor=j
			if minvalor != i:
				A[i], A[minvalor] =A[minvalor], A[i]

>>> A=[4,67,2,45,67,32,13,2,57,1]
>>> ordenamiento_por_selection(A)
>>> print(A)