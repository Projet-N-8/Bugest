import uuid
from Transaction import Transaction
from Depense import Depense
from Recette import Recette

class Personne:
    def __init__(self):
        self._id = str(uuid.uuid4())
        # Relation 1 à n entre 'Personne' et 'Transaction'
        self.transaction_liste = []
        self.depense_liste = []
        self.recette_liste = []

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, valeur: str):
        self._id = valeur

    def ajouter_transaction(self, transaction: Transaction):
        self.transaction_liste.append(transaction)

    def ajouter_depense(self, depense: Depense):
        self.depense_liste.append(depense)

    def ajouter_recette(self, recette: Recette):
        self.recette_liste.append(recette)