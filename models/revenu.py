from transaction import Transaction

class Revenu(Transaction):

    def __init__(self, nom: str, montant: float, date_de_transaction: str = None,
                 categorie: str = None):
        if montant < 0:
            montant = abs(montant)
        super().__init__(nom, montant, date_de_transaction, categorie )
        
