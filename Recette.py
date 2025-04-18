from Transaction import Transaction
from datetime import datetime

class Recette(Transaction):

    def __init__(self, nom: str, montant: float, date_de_transaction: str = None,
                 categorie: str = None):
        if montant < 0:
            montant = abs(montant)
        super().__init__( nom, montant, date_de_transaction, categorie )


recettes = []

rec1 = Recette( "Casino", 1500.0, "2025-04-03" )
rec2 = Recette( "Dividende", -22000.0, date_de_transaction="2025-04-03" )

print(rec1)
print(rec2)

recettes.append(rec1)
recettes.append(rec2)


nom_fichier = "recettes.json"
Recette.sauvegarder_en_json(nom_fichier, recettes)

recettes_chargees = Recette.liste_de_transactions_chargees_a_partir_du_json(
    nom_fichier)

# Affichage
for d in recettes_chargees:
    print(d)