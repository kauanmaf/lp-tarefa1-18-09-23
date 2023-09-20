import unittest
from unittest.mock import patch
import auxiliares

class TestAuxiliares(unittest.TestCase):

    def test_leitura_arquivo(self):
        expected_result = "29 de Janeiro de 2001 - 30 de Janeiro de 2001"
        actual_result = auxiliares.le_arquivo("data.csv")
        self.assertEqual(actual_result, expected_result, "File reading result is incorrect")

    @unittest.expectedFailure
    def test_mes_invalido(self):
        invalid_date = "12 de catacra de 1324 - 15 de maio de 2023"
        result = auxiliares.return_date(invalid_date)
        self.assertEqual(result, invalid_date, "Expected failure: Invalid date format")

if __name__ == "__main__":
    unittest.main()

