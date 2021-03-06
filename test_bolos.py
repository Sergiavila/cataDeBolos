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

	def test_partida_con_spare_ronda_extra(self):
		partida = Partida()
		ronda = [(0,5),(9,1),(5,1),(7,3),(4,3),(5,5),(2,0),(0,0),(0,0),(1,9),[5,3]]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,84)

	def test_partida_con_strike_en_ronda11(self):
		partida = Partida()
		ronda = [(0,0),(6,1),(5,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(10,0),(10,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,43)

	def test_partida_strikes_spares(self):
		partida = Partida()
		ronda = [(5,3),(2,7),(7,3),(5,5),(8,0),(10,0),(10,0),(3,4),(5,5),(2,3)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,119)
	def test_partida_strikes_spare_con_ronda_extra(self):
		partida = Partida()
		ronda = [(0,0),(0,0),(0,0),(10,0),(5,2),(0,0),(3,7),(10,0),(5,0),(10,0),(8,2)]
		resultado = partida.calcularResultado(ronda)
		self.assertEqual(resultado,94)
	def test_una_tirada_tiene_mas_de_10_puntos(self):	
		partida = Partida()
		ronda = [(0,0),(10,3),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = partida.calcularResultado(ronda)
		self.assertFalse(resultado,13)
	def test_partida_con_mas_rondas_no_validas(self):
		partida = Partida()
		ronda = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(10,0),(10,0),(5,2)]
		resultado = partida.calcularResultado(ronda)
		self.assertFalse(resultado,44)

