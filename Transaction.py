from datetime import datetime, date
import json
import uuid

class Transaction:
    def __init__(self,  personne_id: str, nom: str, montant: float, date_de_transaction: str = None,
                categorie: str = None ):
                
        if not personne_id:
            raise ValueError("L'id d'une personne est obligatoire dans chaque transaction")

        self.id = str(uuid.uuid4())
        self.nom = nom
        self.date_de_transaction = date_de_transaction
        self.montant = montant
        self.categorie = categorie
        self._personne_id = personne_id

    @property
    def id(self) -> str:
        return self._id
    
    # Nécessaire pour importer des objets à partir de JSON
    @id.setter
    def id(self, valeur: str):
        self._id = valeur

    @property
    def personne_id(self) -> str:
        return self._personne_id
    


    @property
    def date_de_transaction(self) -> datetime | None:
        return self._date_de_transaction

    @date_de_transaction.setter
    def date_de_transaction(self, valeur: str | None):
        if valeur:
            try:
                self._date_de_transaction = (datetime.strptime(valeur.strip(), '%Y-%m-%d')).date()
            except ValueError:
                raise ValueError("La date doit respecter le format YYYY-MM-DD.")
        else:            
            self._date_de_transaction = None

    @date_de_transaction.deleter
    def date_de_transaction(self):
        print("La date de transaction est réinitialisée à la date d'aujourd'hui par défaut")
        self._date_de_transaction = datetime.now().date()

    @property
    def categorie(self) -> str | None:
        return self._categorie
    
    @categorie.setter
    def categorie(self, valeur: str):
        self._categorie = valeur

    @categorie.deleter
    def categorie(self):
        print("La catégorie est réinitialisée à 'None'.")
        self._categorie = None

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, valeur: str):
        if not valeur:
            raise ValueError("Le nom ne peut pas être vide.")
        self._nom = valeur

    @property
    def montant(self) -> float:
        return self._montant

    @montant.setter
    def montant(self, valeur: float):
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le montant doit être un nombre.")
        self._montant = valeur


    def __str__(self):
        return f"Date:{self._date_de_transaction} | Libellé:{self._nom} | Catégorie:{self._categorie} | {self._montant:.2f}€"

    def __repr__(self):
            return f"{self.date} | {self.nom} | {self.categorie} | {self.montant:.2f}€"

    # Ajouter 'id' dès le début
    def convertir_l_objet_en_dico(self) -> dict:
        dico = { 
            "id": self.id,
            "nom": self.nom,
            "montant": self.montant,
            "date_de_transaction": self.date_de_transaction.strftime('%Y-%m-%d') 
                if self.date_de_transaction else None,
            "categorie": self.categorie,
            "personne_id": self.personne_id
        }
        return dico
    
    # personne_id : obligatoire dans le dictionnaire
    @classmethod
    def convertir_du_dico_en_objet(self, dico:dict):
        if 'personne_id' not in dico:
            raise ValueError("'personne_id' est obbligatoire dans le dictionnaire")

        objet = self(
            personne_id = dico.get('personne_id'),
            nom = dico.get('nom'),
            montant = dico.get('montant'),
            date_de_transaction = dico.get('date_de_transaction'),
            categorie = dico.get('categorie')            
        )
        # objet.id : Récupérer 'id' ou en créer un 'id'
        objet.id = dico.get('id', str(uuid.uuid4()))
        return objet
    
    @classmethod
    def sauvegarder_en_json(self, emplacement_fichier: str,
                            transaction_liste: list):
        with open(emplacement_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(
                [t.convertir_l_objet_en_dico() for t in transaction_liste],
                fichier, ensure_ascii=False, indent = 4
            )

    @classmethod
    def liste_de_transactions_chargees_a_partir_du_json(
        self, emplacement_fichier:str) -> list:
        with open(emplacement_fichier, 'r', encoding='utf-8') as fichier:
            transaction_list = json.load(fichier)
            return [ self.convertir_du_dico_en_objet(transaction)
                    for transaction in transaction_list]



    def convertir_l_objet_en_ligne(self) -> str:
        return f"{self.date.strftime('%Y-%m-%d')} ; {self.nom} ; {self._categorie} ; {self.montant}"

    @classmethod
    def subdiviser_la_ligne_en_objet(self, ligne: str):
        nom, montant_str, date_str, categorie, = ligne.strip().split(";", 4)
        return self( nom, float(montant_str), date_str, categorie )

    @classmethod
    def charger_le_fichier(self, emplacement_fichier: str) -> list:
        depenses = []
        with open(emplacement_fichier, 'r', encoding='utf-8') as fichier:
            for ligne in fichier:
                depense = self.subdiviser_la_ligne_en_objet(ligne)
                depenses.append(depense)
        return depenses

    @staticmethod
    def sauvegarder_dans_le_fichier(emplacement_fichier: str, depense_liste: list):
        with open(emplacement_fichier, 'w', encoding='utf-8') as fichier:
            for depense in depense_liste:
                fichier.write(depense.convertir_l_objet_en_ligne() + '\n')


