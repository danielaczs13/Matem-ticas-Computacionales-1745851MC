def quicksort(arreglo):
	if len(arreglo) == 1 or len(arreglo) == 0:
		return arreglo
	else:
		valor = arreglo[0]
		i= 0
		for j in range(len(arreglo)-1):
			if arreglo[j+1] < valor:
				arreglo[j+1],arreglo[i+1] = arreglo[i+1],arreglo[j+1]
				i += 1
				arreglo[0],arreglo[i] = arreglo[i],arreglo[0]
				p_part = quicksort(arreglo[:i])
				s_part = quicksort(arreglo[i+1:])
				p_part.append(arreglo[i])
				return p_part + s_part

A = [23,57,4,78,43,1,26,44,4,2]
quicksort(A)