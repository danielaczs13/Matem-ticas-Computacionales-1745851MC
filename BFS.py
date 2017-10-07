class fila:
		def __init__(self):
			self.fila=[]
		def obtener(self):
			return self.fila.pop()
		def meter(self,e):
			self.fila.insert(0,e)
			return len(self,fila)
		@property
		def longitud(self):
			return len(self,fila)
		l=fila()
		l.meter(1)
		l.meter(2)
		l.meter(2)
		l.meter(3)
		l.meter(100)
		l.meter(84583)
		print(l.longitud)
		print(l.obtener())
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
def  BFS (g , ni ):
    visitados = []
    f = Fila ()
    f.meter (ni)
    mientras que (f.longi > 0 ):
        na = f.obtener ()
        visitados.append (na)
        ln = g.vecinos [na]
        for nodo in ln:
            if nodo not  in visitados:
                f.meter (nodo)
    return visitados

desm = Grafo ()
desm.conecta ( ' a ' , ' b ' )
pdesm.conecta ( ' c ' , ' a ' )
desm.conecta ( ' d ' , ' b ' )
BFS (desm, ' a ' )
BFS (desm, ' b ' )
desm.E
desm v
