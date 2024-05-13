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

"""

   
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
 

        