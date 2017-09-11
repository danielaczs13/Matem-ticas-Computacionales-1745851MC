#Burbuja
 def burbuja(A):
	for i in range(1, len(A)):
		for j in range(0, len(A)-1):
			if A[j+1]<A[j]:
				aux=A[j]
				A[j]=A[j+1]
				A[j+1]=aux
				print(A)
				#programa principal
				A=[6,5,3,1,8,7,2,4]
				print(A)
				burbuja(A)

#Insercion
def orden_por_insercion(array):
	for indice in range (1, len(array)):
		valor=array[indice] #valor es el eslemnto que vamos a comparar
		i=indice-1	    #i es el valor anterior al elemento que estamos comparando 
		while i>=0: 	   
			if valor<array[i]:  #Comparamos valor con el elemento anterior
				array[i+1]=array[i] #intercambiamos los valores
				array[i]=valor
				i-=1 #Decrementamos en 1 el valor de i
		else:
			break
	return array

A=[26,2,45,30,1,450,1]
orden_por_insercion(A)

#Selection
def selection(arr):
	contador = 0
	for i in range (0, len(arr)-1):
		val = i
		for j in range(i+1, len(arr)):
			contador = contador +1 
			if arr[j] < arr[val]:
				val=j
				if val != i:
					aux=arr[i]
					arr[i]=arr[val]
					arr[val]=aux
					return contador
A= [5,3,5,7,8,12,46,89,57]
selection(A)


#Quick Sort
def quickSort(arreglo):
   quickSort(arreglo,0,len(arreglo)-1)

def quickSort(arreglo,primer,final):
   if primer<final:

       dividir = partir(arreglo,primer,final)

       quickSort(arreglo,primer,dividir-1)
       quickSort(arreglo,dividir+1,final)


def partir(arreglo,primer,final):
   valor = arreglo[primer]

   izquierda = primer+1
   derecha = final

   realizar = F
while
   

       while izquierda <= derecha, [izquierda] <= valor:
           izquierda = izqueirda + 1

       while arreglo[derecha] >= valor, derecha >= izquierda:
           rightmark = rightmark -1

       if derecha < izquierda:
           realizar = V
       else:
           aux = arreglo[izquierda]
           arreglo[izquierda] = arreglo[derecha]
           arreglo[derecha] = aux

   aux = arreglo[primer]
   arreglo[primer] = arreglo[derecha]
   arreglo[derecha] = aux


   return derecha

arreglo = [54,26,93,17,77,31,44,55,20]
quickSort(arreglo)
print(arreglo)