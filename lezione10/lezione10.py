"""
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
"""




#Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione.
#Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
#Classi:
# Film: Rappresenta un film con titolo e durata.
 
# Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

#Metodi:
# prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
# posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
# Cinema: Gestisce le operazioni legate alla gestione delle sale.

#Metodi:
#aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
# prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

#Test case:

#Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
# Un cliente sceglie un film e prenota un certo numero di posti.
#Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

class Film:
    def __init__(self, titolo: str, durata: int) -> None:
        self.titolo=titolo
        self.durata=durata

class Sala:
    def __init__(self, numero_sala: int, film: Film, posti_totali: int) -> None:
        self.numero_sala= numero_sala
        self.film= film
        self.posti_totali=posti_totali
        self.posti_prenotati=0
        self.disponibili=posti_totali
    
    def prenota_posti(self, num_posti): 
        if self.posti_prenotati<self.posti_totali and ((self.posti_totali-self.posti_prenotati)< num_posti):
            self.posti_prenotati+=num_posti
        else:
            return "Non ci sono posti disponibili"

    
    def posti_disponibili(self):
        if self.posti_prenotati==self.posti_totali:
            return "Non ci sono più posti disponibili"
        else:
            self.disponibili=self.posti_totali - self.posti_prenotati
    

class Cinema:
    def __init__(self, sala: Sala, film: Film) -> None:
        self.sala=sala
        self.film=film
        self.sale: list[Sala] = []
    
    def aggiungi_sala(self, sala: Sala):
        if sala  and isinstance (sala, Sala) and sala not in self.sale:
            self.sale.append(sala)

        
    
    def prenota_film(self, titolo_film: str, num_posti):
        if titolo_film == self.film.titolo:
            self.sala.prenota_posti(num_posti)
            return f"posti prenotati: {num_posti}, buona visione"
        else:
            return "Film non in programmazione"
        
cartone: Film= Film(titolo="nemo", durata=160)
sala_1: Sala= Sala(numero_sala=21,film=cartone, posti_totali=23)
lucciola: Cinema=Cinema(sala=sala_1, film=cartone)

sala_1.prenota_posti(34)
lucciola.prenota_film(cartone, 45)
sala_1.posti_disponibili()