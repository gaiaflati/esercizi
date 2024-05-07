"""
class Person:
     def __init__(self, name: str, surname: str, age:int) -> None:
          self.name=name
          self.surname= surname
          self.age= age
name: str= input()
surname: str= input()
age: int = input ()

person= Person(name,surname,age)

print(f"persona con nome= {person.name},cognome= {person.surname}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies: list[str] = []
   
    def add_hobbies(self, hobbies: list[str]):
        self.hobbies.extend(hobbies)

    def add_hobby(self, hobby: str):
        self.hobbies.add(hobby)
    
    def remove_hobby(self, hobby: str):
        if hobby in self.hobbies:
            self.hobbies.remove(hobby)
   
    def __str__(self) -> str:
        return f"person(name={self.name}, age={self.age}, hobbies={self.hobbies})"
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(f"Bob's age is {bob.age}")
if bob.age > alice.age:
    print("Bob is the oldest")
else: 
    print("Alice is the oldest")
luca=Person("Luca", 21)
gaia=Person("Gaia", 23)
oussama=("Oussama", 22)

people=[Person("Gaia", 23),
        Person("Luca", 21),
        Person("Oussama", 22),
        Person("Alice W", 45),
        Person("Bob M", 36)
        ]
age=[]
for person in people:
    if person.age<gaia.age:
        age.append(person.age)
print(f"the youngest is {min(age)}")


class Student:
    def __init__(self, name: str, studyprogram: str):
       self.name=name
       self.studyprogram=studyprogram
       self.age= None
       self.gender= None
    
    def add_age (self, new_age: int):
        self.age= new_age
    
    def add_gender (self, new_gender: str):
        self.gender=new_gender
    
    def __str__(self) -> str:

        print(f"student(name={self.name}, studyprogram={self.studyprogram}, age={self.age}, gender={self.gender})")
    
    
gaia=Student("gaia","Fullstack")
luca=Student("luca", "cloud")
gimmy=Student("gimmy", "cyber security")

gaia.add_age(23)
luca.add_age(21)
gimmy.add_age(27)
gaia.add_gender("girl")
luca.add_gender("boy")
gimmy.add_gender("boy")



print(luca)
print(gaia)
print(gimmy)
"""

class Animal:
    def __init__(self, name: str, legs: int) -> None:
        self.name=name
        self.legs=legs
    def setLegs(self, settedlegs):
        self.legs=settedlegs
    def getLegs (self):
        return self.legs
    def __str__(self) -> str:
        return f"{self.name.capitalize()}(legs={self.getLegs()})"

dog=Animal("dog", 4)
print (dog)
cat=Animal("cat", 4)
print(cat)

class Food:
    def __init__(self, name: str, price: int, description: str) -> None:
        self.name=name
        self.price= price
        self.description=description
    
    def __str__(self) -> str:
        return f'{self.name.capitalize()}(price={self.price}, descr={self.description})'
pasta=Food("pasta",10.00, "primo")
pollo=Food("pollo",14.99, "secondo")
cicoria=Food("cicoria", 6, "contorno")

class Menu:
    def __init__(self, foods: list[Food]) -> None:
        self.foods=foods
    
    def add_food(self, food):
        self.food.append(food)
    
    def remove_food(self, food):
        if food in self.foods:
            self.foods.remove(food)
    def __str__(self) -> str:
        pass
pizza=Menu([pollo, cicoria, pasta])
    
