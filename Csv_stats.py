import csv

def somme_des_montants(emplacement_fichier: str, condition) -> float:
    with open(emplacement_fichier, newline='') as fichier_csv:
        reader = csv.reader(fichier_csv, delimiter=',')
        # Sauter la première ligne (le header)
        next(reader)  
        total = 0.0
        for ligne in reader:
            try:
                montant = float(ligne[1])
                if condition(montant):
                    total += montant
            except (ValueError, IndexError):
                # Sauter les lignes contenant des données invalides
                continue  
        return total
    

def somme_des_recettes(emplacement_fichier: str) -> float:
    return somme_des_montants(emplacement_fichier, lambda x: x > 0)

def sommes_des_paiements(emplacement_fichier: str) -> float:
    return somme_des_montants(emplacement_fichier, lambda x: x < 0)
