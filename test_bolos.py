import unittest

from bolos import Partida
class PartidaBolos(unittest.TestCase):
	def test_partida_simple(self):
		partida = Partida()
		ronda = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,0)

