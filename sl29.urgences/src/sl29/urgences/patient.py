class Patient:
    def __init__(self, id:int, nom:str, gravite:int, symptome:str) -> None:
        self._identifiant = id
        self._nom = nom
        self._gravite = gravite
        self._symptome = symptome

    def __repr__(self) -> str:
        return f"Nom : {self.nom}, Id : {self.identifiant}, Symptome : {self.symptome}"

    @property
    def identifiant(self):
        return self._identifiant

    @property
    def nom(self):
        return self._nom

    @property
    def gravite(self):
        return self._gravite

    @property
    def symptome(self):
        return self._symptome