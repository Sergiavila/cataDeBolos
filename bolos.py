class Partida():
	def calcularResultado(self,ronda):
		suma = 0
		for i in range(0, len(ronda)):
			if sum(ronda[i]) <= 10:
				if i == 9:
					if(ronda[i][0] == 10):
						suma += sum (ronda[i]) + sum(ronda[i+1])
					elif(sum(ronda[i]) == 10 and ronda[i][0] != 10):
						suma += sum(ronda[i]) + ronda[i+1][0]
					else:
						suma += sum(ronda[i])
				elif i < 9:
					if(ronda[i][0] == 10):
						suma += sum (ronda[i]) + sum(ronda[i+1])
					elif(sum(ronda[i]) == 10 and ronda[i][0] != 10):
						suma += sum(ronda[i]) + ronda[i+1][0]
					else:
						suma += sum(ronda[i])
				else:
						suma += sum(ronda[i])
		return suma
