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


class ContoBancario:

    total_accounts=0

    def __init__(self, iban, saldo, nome) -> None:
        self.iban= iban
        self.saldo= saldo
        self.nome= nome

        ContoBancario.total_accounts += 1
    
    def deposito(self, importo):
        self.saldo += importo
        print(f"{importo} depositato. il nuovo saldo è {self.saldo}")
    
    def prelievo(self, importo):
        self.saldo -= importo
        print(f"{importo} prelevato. il nuovo saldo è {self.saldo}")

    @classmethod
    def get_total_accounts(cls):
        print(f"Account totali creati: {cls.total_accounts}")

    @classmethod
    def get_type(cls):
        print(f"type: {cls.definizione}")

    @staticmethod
    def valida_account(iban):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print("iban valido")
            return True
        else:
            print("iban non valido")
            return False
        
account1= ContoBancario(123456789, 0, "Alice")
account2= ContoBancario(9876543210, 1000, "Bob")

account1.deposito(500)
account2.prelievo(200)

ContoBancario.get_total_accounts()