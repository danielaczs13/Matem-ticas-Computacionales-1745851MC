class Pila:
	def __init__(self):
		self.items=[]
		def apilar(self, x):
			self.items.append(x)
			def desapilar(self):
				try:
					return self.items.pop()
				except IndexError:
					raise ValueError("La pila est� vac�a")
				def es_vacia(self):
					return self.items == []

