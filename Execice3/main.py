
from csv_reader import *

def main():

    try:
        articles = charger_csv("articles.csv")

        print("Liste des articles :")

        for article in articles:
            print(article)

    except FichierIntrouvableException as e:
        print("Erreur fichier :", e)

    except LigneInvalideException as e:
        print("Erreur ligne :", e)

    except PrixNegatifException as e:
        print("Erreur prix :", e)

if __name__ == "__main__":
    main()
