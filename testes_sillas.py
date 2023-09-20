


import unittest
from unittest.mock import patch
import auxiliares


class Auxiliares(unittest.TestCase):
    def leitura_arquivo(self):
        self.assertEqual(auxiliares.le_arquivo("data.csv"), "29 de Janeiro de 2001 - 30 de Janeiro de 2001")

    def mes_invalido(self):
        self.assertEqual(auxiliares.return_date("12 de catacra de 1324 - 15 de maio de 2023"),
                         "12 de catacra de 1324 - 15 de maio de 2023")


if __name__ == "__main__":
    unittest.main()


