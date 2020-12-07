class Partida():
	def calcularResultado(self,ronda):
		suma = 0
		for i in range(0, len(ronda)-1):
			suma += sum(ronda[i])
		return suma
