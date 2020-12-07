import unittest

from bolos  import Partida
class PartidaBolos(unittest.TestCase):
	def test_dummy(self):
		partida = Partida()
		resultado = partida.calcularResultado()
		self.assertEqual(resultado,0)
