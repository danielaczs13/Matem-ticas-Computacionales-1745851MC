def burbuja(lista):
    cnt=0
    for i in range(0, len(lista) - 1):
        for j in range (0, len(lista) - 1):
            cnt += 1
            if (lista[j + 1]) < lista[j]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return cnt

def insercion(lista):
    cnt=0
    for indice in range (1, len(lista)):
        posicion  = lista[indice]
        i = indice - 1
        while i >= 0:
            cnt += 1
            if posicion < lista[i]:
                lista[i + 1] = lista[i]
                lista [i] = posicion
                i -= 1
            else:
                break
    return cnt

def selection(lista):
    cnt = 0
    for i in range(0, len(lista) - 1):
	    valor = i
	    for j in range(i + 1, len(lista)):
	    	if lista[j] < lista[valor]:
    			valor = j
                cnt += 1
	    if valor != i:
		    aux = lista[i]
		    lista[i] = lista[valor]
		    lista[valor] = aux
    return cnt


def quicksort(lista):
    cnt=0
    if len(lista)<=1:
        return lista
    p=lista.pop(0)
    men,may =[],[]
    for e in lista:
        cnt+=1
        if e<=p:
            men.append(e)
        else:
            may.append(e)
    return cnt

import random
def randomlista(lista):
    a=[]
    for i in range(lista):
        a.append(random.randint(0,lista))
    return a

import copy
lonarr = 10
while lonarr < 1000:
    for i in range(1,30):
        arreglo = randomlista(lonarr)
        aa,ab,ac,ad = copy.deepcopy(arreglo),copy.deepcopy(arreglo),copy.deepcopy(arreglo),copy.deepcopy(arreglo)
        bsort=burbuja(aa)
        isort=insercion(ab)
        ssort=selection(ac)
        qsort=quicksort(ad)
        print(lonarr,bsort,isort,ssort,qsort)
    lonarr*=2