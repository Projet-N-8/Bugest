import json
import os
from flask import current_app
from datetime import date
from models.personne import Personne

def lire_personnes():
    try:
        with open(current_app.config['DATA_FILE'], 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Erreur: Le fichier JSON '{current_app.config['DATA_FILE']}' est corrompu ou vide. Initialisation avec une liste vide.")
        return []

def ecrire_personnes(data):
    os.makedirs(os.path.dirname(current_app.config['DATA_FILE']), exist_ok=True)
    with open(current_app.config['DATA_FILE'], 'w') as f:
        json.dump(data, f, indent=4)

def ajouter_nouvelle_personne(mail, nom, prenom, date_naissance_str, sexe):
    try:
        date_naissance = date.fromisoformat(date_naissance_str)
        personne = Personne(mail, nom, prenom, date_naissance, sexe)
        personne_dict = {
            "mail": personne.mail,
            "nom": personne.nom,
            "prenom": personne.prenom,
            "date_naissance": personne.date_naissance.isoformat(),
            "sexe": personne.sexe
        }

        personnes = lire_personnes()
        personnes.append(personne_dict)
        ecrire_personnes(personnes)
        return True, personne.prenom, personne.nom
    except ValueError as e:
        return False, str(e), None
    except Exception as e:
        return False, f"Une erreur inattendue s'est produite: {e}", None