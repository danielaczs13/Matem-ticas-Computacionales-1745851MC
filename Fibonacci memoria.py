arreglo={}
cnt=0
def fibonacci(n):
	global arreglo, cnt
	cnt+=1
	if n==0 or n==1:
		return(1)
	if n in arreglo:
		return arreglo[n]
	else:
		aux=fibonacci(n-1) + fibonacci(n-2)
		arreglo[n]=aux
		return aux
	
	for i in range(2, 30):
		cnt=0
		print(i, fibonacci(i), cnt)
