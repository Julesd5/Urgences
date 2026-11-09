from patient import Patient
from sl29.structures.queue import Queue 
from typing import Optional

class StructureUrgences:
    def __init__(self) -> None:
        self._prio0 = Queue()
        self._prio1 = Queue()
        self._prio2 = Queue()
        self._prio3 = Queue()
        self._prio4 = Queue()

    def __repr__(self) -> str:
        return (
            f"0:{self._prio0!r}\n1:{self._prio1!r}\n2:{self._prio2!r}\n"
            f"3:{self._prio3!r}\n4:{self._prio4!r}\n"
        )
    
    def est_vide(self) -> bool:
        return self._prio0.is_empty() and self._prio1.is_empty() and self._prio2.is_empty() and self._prio3.is_empty() and self._prio4.is_empty()

    def taille(self) -> tuple:
        return (self._prio0.size(), self._prio1.size(), self._prio2.size(), self._prio3.size(),self._prio4.size())

    def defiler(self) -> Optional['Patient']:
            for i in range(5):
                if not self._mapping()[i].is_empty(): # type: ignore
                    return self._mapping()[i].dequeue() # type: ignore
            return None # optionnel return None si il n'y a aucun patient

    def enfiler(self, patient) -> None:
        prio = patient.gravite
        queue = self._mapping()[prio]
        queue.enqueue(patient)

    def _mapping(self):
        return {0:self._prio0, 1:self._prio1, 2:self._prio2, 3:self._prio3, 4:self._prio4}