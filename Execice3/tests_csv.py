
import unittest
import os

from csv_reader import *


class TestCsv(unittest.TestCase):

    def test_csv_valide(self):
        with open("test.csv", "w") as f:
            f.write("1;PC;5000\n2;Souris;80")

        articles = charger_csv("test.csv")

        self.assertEqual(len(articles), 2)
        os.remove("test.csv")

    def test_fichier_absent(self):
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("inexistant.csv")

    def test_prix_texte(self):
        with open("test.csv", "w") as f:
            f.write("1;PC;abc")

        with self.assertRaises(LigneInvalideException):
            charger_csv("test.csv")

        os.remove("test.csv")

    def test_prix_negatif(self):
        with open("test.csv", "w") as f:
            f.write("1;PC;-100")

        with self.assertRaises(PrixNegatifException):
            charger_csv("test.csv")

        os.remove("test.csv")


if __name__ == "__main__":
    unittest.main()
