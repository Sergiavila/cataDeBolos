class Partida():
	def calcularResultado(self,ronda):
		suma = 0
		for i in range(0, len(ronda)):
			if(ronda[i][0] == 10):
				suma += sum (ronda[i]) + sum(ronda[i+1])
			else:
				suma += sum(ronda[i])
		return suma
