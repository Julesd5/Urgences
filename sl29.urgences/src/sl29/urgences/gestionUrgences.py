from patient import Patient
from structureUrgences import StructureUrgences
from typing import Any, Optional

class GestionUrgence:
    def __init__(self) -> None:
        self._structure = StructureUrgences()

    def __repr__(self) -> str:
        return repr(self._structure)

    def inserer_patient(self, id:int, nom:str, gravite:int, symptome:str) -> None:
        p = Patient(id, nom, gravite, symptome)
        self._structure.enfiler(p)
        
    def traiter_patient(self):
        return self._structure.defiler()

    def est_vide(self) -> bool:
        return self._structure.est_vide()