


import unittest
from unittest.mock import patch
import main_fuc

class Teste_Le_Arquivo(unittest.TestCase):
    @patch('builtins.input', side_effect=['data.csv'])
    def leitura_arquivo(self, mock_input):
        resultado = main_fuc.input_func()
        self.assertEqual(resultado, 1)



if __name__ == "__main__":
    unittest.main()




