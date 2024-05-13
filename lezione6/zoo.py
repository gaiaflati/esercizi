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
        self.area_animal=height*width #inserire i get

class Fence:
    def __init__(self, area: int, temperature: int, habitat: str) -> None:
        self.area=area
        self.temperature=temperature
        self.habitat=habitat

class Zookeper:
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name=name
        self.surnmae=surname
        self.id=id
    
    def add_animal(self, animal: Animal, fence: list):
        fence: list=[]
        if animal and isinstance(animal, Animal) and animal not in fence:
            if Animal.area_animal<= Fence.area and Animal.preferred_habitat==Fence.habitat:   #richiamare con i get
                fence.append(animal)
                Fence.area-=Animal.area_animal
            


        

class Zoo:
    def __init__(self, fences: Fence, zoo_keepers: Zookeper) -> None:
        self.fences=fences
        self.zoo_keepers=zoo_keepers        