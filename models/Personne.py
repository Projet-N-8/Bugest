from datetime import date

class Personne:
    def __init__(self, mail: str, nom: str, prenom: str, sexe: str, date_naissance: date):
        self.mail = mail #Servira de clé primaire dans la programmation
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date_naissance = date_naissance
    
    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, value: str):
        self._nom = value.strip()

    @property
    def prenom(self) -> str:
        return self._prenom

    @prenom.setter
    def prenom(self, value: str):
        self._prenom = value.strip()

    @property
    def sexe(self) -> str:
        return self._sexe

    @sexe.setter
    def sexe(self, value: str):
        if value not in ['M', 'F', 'X']:
            raise ValueError("Le sexe doit être soit M, F ou X")
        self._sexe = value

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, value: date):
        self._date_naissance = value