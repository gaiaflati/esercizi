"""
class Animal: 
    
    def __init__(self, specie: str, age: int) -> None:
        
        self.specie=specie
        self.age=age
    
    def __str__(self) -> str:
        f" {self.__class__.__name__}(name={self.name}, età={self.age}, specie={self.specie})"

    
    
class Person(Animal): 
    
    def __init__(self, age: int, cf: str, name: str, surname: str, specie: str,) -> None:
        super().__init__(specie, age)

        self.cf=cf
        self.name= name
        self.surname= surname

    def speak(self) -> str:
        return f" Ciao mi chiamo {self.name} {self.surname} e ho {self.age} anni."

    def __str__(self) -> str:
        s: str= super().__str__()[:-1]
        s += f", surname={self.surname}, cf={self.cf}"
        return s
        


class Cat(Animal):
        
    def __init__(self, age: int, name: str, specie="Felidae") -> None:
        super().__init__(specie, age,)
        self.name=name

    def __str__(self) -> str:
        return f"Cat--> (nome={self.name}, age={self.age}, specie={self.specie} )"
    
class Rabbit(Animal):
    
    def __init__(self, age: int, name: str) -> None:
        super().__init__("Leporidae", age)
        self.name=name





p= Person(name="Gaia", surname="Flati", cf="FLTGAI01C53H5010", age=23)
a=Animal(specie="balena", age=26)



   
class Room:

    def __init__(self, id, floor, seats) -> None:
        self.id=id
        self.floor=floor
        self.seats=seats
    
    def get_floor(self):
        return self.floor
    
    def get_seats(self):
        return self.seats
    
    def get_id(self):
        return self.id

    def __str__(self) -> str:
        return f"Room(id={self.id}, floor={self.floor}, seats={self.seats})"


class Building:
   
    def __init__(self, name: str, address: str, num_floor: int, rooms: list= []) -> None:
        self.name= name
        self.address=address
        self.rooms=rooms
        self.num_floors=num_floor
    
    def get_num_floors(self):
        return self.num_floors

    def add_room(self, room: Room):
        if room and isinstance(room, Room) and room not in self.rooms and room.get_floor() <= self.get_num_floors():
            self.rooms.append(room)
    
    def are(self) -> float:
        sum_area: float= 0
        for room in self.rooms:
            sum_area += room.get_area()
        return sum_area

    def __str__(self) -> str:
        return f"{self.name} @ {self.address}"
    

class Groups:
    def __init__(self, name: str, limit: int) -> None:
        self.name=name
        self.limit=limit
        self.students: list[Student]=[]
   
    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def add_student(self, student: Student)
        limit: int= self.get_limit()
        if student and isinstance(student, Student)

        


smi= Building (name="SMI", address="Via Sierra Nevada 60", num_floors=5)
armellini=Building (name="ITIS", address="Basilica San Paolo", num_floor=3, rooms=[])

smi.add_room(Room(id="666", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room)
smi.add_room(None)



def symmetric(tree: list[int]) -> bool:
    destra=[]
    i=0
    for i in range(len(tree)):
        destra.append[tree[2*i+1]]
        i+=1
    sinistra=[]
    i=0
    while i<= len(tree):
        sinistra.append[tree[2*(i+1)]]
        i+=1
    if destra==sinistra:
        return True
    else:
        return False
    
print(symmetric([1,2,2,3,4,4,3]))
 

def symmetric(tree: list[int]) -> bool:
    i=0
    destra=[]
    for i in range(len(tree)):
        if tree[2*i+1] == tree [2*(i+1)]:
            i=5
            return True
        else:
            return False
        
def calcola_stipendio(ore_lavorate: int) -> float:
    # cancella pass e scrivi il tuo codice
    if ore_lavorate<=40.00:
        stipendio=ore_lavorate*10.00
    else:
        stipendio=400.00+ (ore_lavorate-40.00)*15.00
    
    return ore_lavorate


def seconds_since_noon(ore: int, minuti: int, secondi: int) -> int:
   
        secondi_=ore*3600+minuti*60+secondi
        return secondi_
seconds_since_noon(1,0,0)
        
def time_difference(ore, minuti, secondi, ore_2, minuti_2, secondi_2):
    orario_1=seconds_since_noon(ore, minuti, secondi)
    orario_2=seconds_since_noon(ore_2, minuti_2, secondi_2)
    print (orario_1, orario_2)
    time= orario_2-orario_1
    return time
print(time_difference(1, 0, 0, 3, 15, 30))



class LinkedList:
   
    def __init__(self, Node: str) -> None:
        self.Node=Node

        
def is_palindrome(head: Node) -> list[int]:
"""
def merge(nums1, m, nums2, n):
    for i in nums2:
        nums1.append[i]
    if len(nums1)!=m+n:
        nums1.remove(0)
    return nums1

merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(nums1)  

 #- push(x: int) -> None: Pushes element x to the top of the stack.
# pop() -> None Removes the element on the top of the stack and returns it.
# top() -> None Returns the element on the top of the stack.
# empty() -> None Returns true if the stack is empty, false otherwise.

class MyStack:
    def __init__(self, elements=[]):
        self.elements=elements
        
    def push(self, x: int) ->None:
        for i in self.elements:
            if i==x:
                self.elements.append(x)

    def pop(self):
        return self.elements.pop(-1)
        
    def top(self):
        return self.elements[-1]
    
    def empty(self):
        if len(self.elements)==0:
            return True
        else:
            False