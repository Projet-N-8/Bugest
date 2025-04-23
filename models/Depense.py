from Transaction import Transaction

class Depense(Transaction):

    def __init__(self, personne_id: str, nom: str, montant: float, date_de_transaction: str = None,
                 categorie: str = None):
        if montant > 0:
            montant = -abs(montant)
        super().__init__( personne_id, nom, montant, date_de_transaction, categorie )
