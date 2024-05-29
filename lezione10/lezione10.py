from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    @abstractmethod
    def verso():

        pass

class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super().__init__()

        self.nome= nome 

    def verso(self):
        return print("Bau!")
    
cane__1: Cane = Cane(nome="Pluto")
cane__1.verso()

class Gatto(AbcAnimal):
    
    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome=nome
    
    def verso(self):
        return print("Miao!")

gatto: Gatto= Gatto(nme="micio")
gatto.verso()