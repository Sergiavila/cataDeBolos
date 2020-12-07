import unittest

from bolos import Partida
class PartidaBolos(unittest.TestCase):
	def test_partida_simple(self):
		partida = Partida()
		ronda = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,0)

	def test_partida_1_punto(self):
		partida = Partida()
		ronda = [(0,0),(0,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,1)

	def test_partida_varios_puntos(self):
		partida = Partida()
		ronda = [(3,2),(0,1),(0,5),(6,1),(2,3),(4,5),(6,0),(0,0),(0,0),(0,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,38)

