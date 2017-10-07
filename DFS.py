class Pila:
		def __init__(self):
			self.items=[]
			def apilar(self, x):
				self.items.append(x)
				def desapilar(self):
					try:
						return self.items.pop()
					except IndexError:
						raise ValueError("La pila está vacía")
					def es_vacia(self):
						return self.items == []

class Grafo:
    def __init__(lista):
        lista.V = set() # un conjunto
        lista.E = dict() # un mapeo de pesos de aristas
        lista.vecinos = dict() # un mapeo
 
    def agrega(lista, v):
        lista.V.add(v)
        if not v in lista.vecinos: # vecindad de v
            lista.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(lista, v, u, valor=1):
        lista.agrega(v)
        lista.agrega(u)
        lista.E[(v, u)] = lista.E[(u, v)] = valor # en ambos sentidos
        lista.vecinos[v].add(u)
        lista.vecinos[u].add(v)
 
    def complemento(lista):
        comp= Grafo()
        for v in lista.V:
            for w in lista.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp
def  DFS ( g , ni ):
    visitados = []
    f = Pila ()
    f.meter (ni)
    while (f.long > 0 ):
        na = f.obtener ()
        visitados.append (na)
        ln = g.vecinos [na]
        for nodo in ln:
            if nodo not  in visitados:
                f.meter (nodo)
    return visitados

desm. = Grafo ()
desm.conecta ( ' a ' , ' b ' )
desm.conecta ( ' c ' , ' a ' )
desm.conecta ( ' d ' , ' b ' )
DFS (desm, ' a ' )
DFS (desm, ' b ' )
desm.E
desm v
