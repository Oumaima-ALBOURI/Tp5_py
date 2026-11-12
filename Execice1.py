# 1. Exception personnalisée
class NomException(Exception):
    def __init__(self, message):
        super().__init__(message)


# 2. Classe principale
class NomClasse:

    # Constructeur
    def __init__(self, attribut1, attribut2):
        self.attribut1 = attribut1
        self.attribut2 = attribut2

    # Méthode 1
    def methode1(self):
        pass

    # Méthode 2
    def methode2(self):
        if condition:
            raise NomException("Message d'erreur")

    # Méthode d'affichage
    def afficher(self):
        pass


# 3. Programme principal
try:
    objet = NomClasse(valeur1, valeur2)
    objet.afficher()
    objet.methode1()
    objet.methode2()

except NomException as e:
    print("Erreur:", e)