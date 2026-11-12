
# Exceptions personnalisées

class CsvException(Exception):
    def __init__(self, message):
        super().__init__(message)


class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass


# Fonction de lecture CSV

def charger_csv(chemin):

    articles = []

    try:
        with open(chemin, "r", encoding="utf-8") as fichier:

            for numero, ligne in enumerate(fichier, start=1):

                if not ligne.strip():
                    continue

                colonnes = ligne.strip().split(";")

                if len(colonnes) != 3:
                    raise LigneInvalideException(
                        f"Ligne {numero} invalide."
                    )

                id_article, nom, prix = colonnes

                try:
                    prix = float(prix)
                except ValueError:
                    raise LigneInvalideException(
                        f"Prix non numérique à la ligne {numero}."
                    )

                if prix <= 0:
                    raise PrixNegatifException(
                        f"Prix invalide à la ligne {numero}."
                    )

                article = {
                    "id": id_article,
                    "nom": nom,
                    "prix": prix
                }

                articles.append(article)

    except FileNotFoundError:
        raise FichierIntrouvableException(
            "Fichier CSV introuvable."
        )

    return articles
