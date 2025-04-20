
from Personne import Personne
from Transaction import Transaction
from Depense import Depense
from Recette import Recette

def creer_deux_personnes():
    p1 = Personne()
    p2 = Personne()
    return p1, p2

def generer_des_transactions_par_personne():
    # Créer 2 instances de Personne, les retouner avec leurs id
    p1, p2 = creer_deux_personnes()
    # Créer des transactions à partir de la classe transaction
    t1 = Transaction( p1.id, "Loyer", -1000.0, "2025-04-03" )
    t2 = Transaction( p1.id, "Electricité", -220.0, date_de_transaction="2025-04-03" )
    t3 = Transaction( p2.id, "Diésel", -80.00, "2025-04-04", categorie="Carburant" )
    # Manipulation sur une transaction
    del t3.date_de_transaction      # Réinitialise la date
    del t3.categorie                # Réinitialise la catégorie
    # Ajouter plusieurs transactions et les rattacher à une personne spécifique
    # Chaque personne possède de 0 à N transactions
    p1.ajouter_transaction(t1)
    p1.ajouter_transaction(t2)
    p2.ajouter_transaction(t3)

    transaction_par_personne = "\nAfficher l'identifiant de chaque transaction en les regroupant par personne"
    print( transaction_par_personne + "\n" + "_"  * ( len( transaction_par_personne ) - 1 ) )
    num_transaction = "Transaction N°"
    num_personne = "| Personne N°"
    print( "\nTransaction de la première personne")
    for t in p1.transaction_liste:
        print( num_transaction, t.id, num_personne, t.personne_id )

    print( "\nTransaction de la deuxième personne")
    for t in p2.transaction_liste:
        print( num_transaction, t.id, num_personne, t.personne_id )

    transaction_reliee_a_une_personne = "\nAfficher l'identifiant de chaque transaction en connaissant à qui elle est rattachée"
    print( transaction_reliee_a_une_personne + "\n" + "_" * ( len( transaction_reliee_a_une_personne) - 1 ) )
    print( num_transaction, t1.id, num_personne, t1.personne_id )
    print( num_transaction, t2.id, num_personne, t2.personne_id )
    print( num_transaction, t3.id, num_personne, t3.personne_id, "\n" )

    # Affichage des transactions
    print(t1)
    print(t2)
    print(t3)

def sauvegarder_et_charger_les_depenses_en_json():    
    # Obtenir les id de 2 instances de Personne
    p1, p2 = creer_deux_personnes()

    dep1 = Depense( p1.id, "Loyer", -1000.0, "2025-04-03" )
    dep2 = Depense( p2.id, "Electricité", -220.0, date_de_transaction="2025-04-03" )

    print("\nDépenses")
    print(8 * "_" + "\n")
    print(dep1)
    print(dep2)

    depenses = []
    depenses.append(dep1)
    depenses.append(dep2)

    nom_fichier = "depenses.json"
    Depense.sauvegarder_en_json(nom_fichier, depenses)

    depenses_chargees = Depense.liste_de_transactions_chargees_a_partir_du_json(
        nom_fichier)

    # Affichage des dépenses chargée à partir du json
    for d in depenses_chargees:
        print(d) 


def sauvegarder_et_charger_les_recettes_en_json():
    recettes = []
    # Obtenir les id de 2 instances de Personne
    p1, p2 = creer_deux_personnes()

    rec1 = Recette( p1.id, "Casino", 1500.0, "2025-04-03" )
    rec2 = Recette( p2.id, "Dividende", -22000.0, date_de_transaction="2025-04-03" )

    print("\nRecettes")
    print(8 * "_" + "\n")
    print(rec1)
    print(rec2)

    recettes.append(rec1)
    recettes.append(rec2)

    nom_fichier = "recettes.json"
    Recette.sauvegarder_en_json(nom_fichier, recettes)

    recettes_chargees = Recette.liste_de_transactions_chargees_a_partir_du_json(
        nom_fichier)

    # Affichage des dépenses chargée à partir du json
    for d in recettes_chargees:
        print(d)

def main():
    generer_des_transactions_par_personne()
    sauvegarder_et_charger_les_depenses_en_json()
    sauvegarder_et_charger_les_recettes_en_json()

if __name__ == "__main__":
    main()

