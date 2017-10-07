Grafo:
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
