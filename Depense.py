from Transaction import Transaction
from datetime import date
import json

class Depense(Transaction):

    def __init__(self, nom: str, montant: float, date_de_transaction: str = None,
                 categorie: str = None):
        if montant > 0:
            montant = -abs(montant)
        super().__init__( nom, montant, date_de_transaction, categorie )

depenses = []

dep1 = Depense( "Loyer", -1000.0, "2025-04-03" )
dep2 = Depense( "Electricité", -220.0, date_de_transaction="2025-04-03" )

print(dep1)
print(dep2)

depenses.append(dep1)
depenses.append(dep2)

nom_fichier = "depenses.json"
Depense.sauvegarder_en_json(nom_fichier, depenses)

depenses_chargees = Depense.liste_de_transactions_chargees_a_partir_du_json(
    nom_fichier)

# Affichage
for d in depenses_chargees:
    print(d)

'''
depenses_liste_de_dico = []
for depense in depenses: 
    dico = {}
    for cle, valeur in depense.__dict__.items():
        if isinstance(valeur, date):
            dico[cle] = valeur.strftime('%Y-%m-%d')
        else:
            dico[cle] = valeur
    depenses_liste_de_dico.append(dico)

# ASCII = False pour préserver les caractères accentuées : ç | à | é | è | ...
# Les 2 lignes suivantes ne sont pas obligatoires, elles servent à montrer le résultat joliment dans la console
json_dico = json.dumps( depenses_liste_de_dico, ensure_ascii=False, indent=4 )
print(json_dico)
# Sauvegarder la liste des dépenses dans un fichier JSON
with open('depenses.json', 'w', encoding='utf-8') as fichier:
    json.dump(depenses_liste_de_dico, fichier, ensure_ascii=False, indent=4)

'''


''' Version avec compréhension de liste qui sera sans doute trop compliquée à expliquer
json_string = json.dumps( [
    {
        k: v.strftime('%Y-%m-%d') if isinstance(v, date) else v
        for k, v in depense.__dict__.items()
    }
 for depense in depenses ] )
print(json_string)
'''