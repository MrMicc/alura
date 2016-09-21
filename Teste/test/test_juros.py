from unittest import TestCase
from Teste.juros import Juros


class TestJuros(TestCase):
    def test_simples(self):
        calc_juros = Juros()
        calc_juros.set_capital(16000)
        calc_juros.set_n_periodo(4)
        calc_juros.set_taxa(0.04)
        self.assertEqual(2560.0, calc_juros.simples())
