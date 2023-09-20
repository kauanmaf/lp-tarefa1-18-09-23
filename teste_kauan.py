import unittest
import main as ut
from main import *
# Teste automático x Teste Manual



class TestFatorial(unittest.TestCase):
    # Equivalence Partitioning Method

    # Equivalence Class Method
    # Testar as partições, apenas 1 já é suficiente
    def teste_data_negativa(self):
        self.assertEqual(ut.aux,120)
    
    def test_lesser_than_0(self):
        self.assertEqual(ut.fatorial(-1),1)

    # Boundary Value Analysis ou Boundary Value Test
    def test_equal_to_0(self):
        self.assertEqual(ut.fatorial(0),1)

    def test_equal_to_1(self):
        self.assertEqual(ut.fatorial(1),1)
    
    # data type test
    def test_input_value_type(self):
        self.assertRaises(TypeError, ut.fatorial, "oi")


if __name__== "__main__":
    unittest.main()