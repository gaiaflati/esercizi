"""
Classi:
1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: 
name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. 
I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali,
pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.


1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): 
consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo.
L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat
e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, 
ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto 
ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

"""


class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: int) -> None:
        self.name=name
        self.species=species
        self.age=age 
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.health=round(100* (1/age), 3)
        self.area_animal=round(height*width, 3) #inserire i get
        self.fence=None

class Fence:
    def __init__(self, area: int, temperature: int, habitat: str) -> None:
        self.area=area
        self.temperature=temperature
        self.habitat=habitat
        self.list_animals=[]
        self.area_rimanente=area

class Zookeper:
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name=name
        self.surnmae=surname
        self.id=id
    
    def add_animal(self, animal: Animal, fence: Fence):
        if animal and isinstance(animal, Animal) and animal not in fence:
            if animal.area_animal<= fence.area and animal.preferred_habitat==fence.habitat:   #richiamare con i get
                fence.list_animals.append(animal)
                fence.area_rimanente = fence.area-animal.area_animal
                animal.fence=fence
    
    def remove_animal(animal: Animal, fence: Fence):
        if animal and isinstance(animal, Animal) and animal in fence:
             fence.list_animals.remove(animal)
             fence.area+=animal.area_animal

    def feed(animal: Animal):
        animal.height+= round((animal.height*2/100), 3)
        animal.width+= round((animal.width*2/100), 3)
        if (animal.height*animal.width) <= animal.fence:
            animal.health+= round((animal.health*1)/100, 3)
            





        

class Zoo:
    def __init__(self, fences: Fence, zoo_keepers: Zookeper) -> None:
        self.fences=fences
        self.zoo_keepers=zoo_keepers        