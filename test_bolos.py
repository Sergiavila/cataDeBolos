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

	def test_partida_con_strike(self):
		partida = Partida()
		ronda = [(3,2),(0,1),(0,5),(6,1),(2,3),(4,5),(6,0),(0,0),(10,0),(3,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,54)

	def test_partida_con_strike2(self):
		partida = Partida()
		ronda = [(3,2),(0,1),(0,5),(6,1),(0,0),(4,5),(6,0),(10,0),(5,3),(3,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,62)

	def test_partida_con_strike_ronda_extra(self):
		partida = Partida()
		ronda = [(3,2),(0,1),(0,5),(6,1),(0,0),(4,5),(6,0),(10,0),(5,3),(10,0),(5,4)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,87)

	def test_partida_con_spare(self):
		partida = Partida()
		ronda = [(0,0),(9,1),(5,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,21)

	def test_partida_con_spare2(self):
		partida = Partida()
		ronda = [(0,5),(9,1),(5,1),(7,3),(4,3),(5,5),(2,0),(0,0),(0,0),(0,9)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,70)

