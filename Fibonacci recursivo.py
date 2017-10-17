cnt=0
def fibonacci(n):
	global cnt
	cnt+=1
	if n==0 or n==1:
		return(1)
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	for i in range(2, 30):
		cnt=0
		print(i, fibonacci(i), cnt)


		