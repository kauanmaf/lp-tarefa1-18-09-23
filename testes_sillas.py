


import unittest
from unittest.mock import patch

class Teste_Le_Arquivo(unittest.TestCase):
    @patch('builtins.input', side_effect=['data.csv'])
    def leitura_arquivo(self):
        import main
        self.assertEqual()






if __name__ == "__main__":
    unittest.main()




