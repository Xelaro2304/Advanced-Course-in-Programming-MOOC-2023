# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        if self.persons == []:
            return True
        else: 
            return False
    
    def print_contents(self):
        for person in self.persons:
            print(f'{person} ({person.height} cm)')

    def shortest(self):
        if self.is_empty():
            return None
        else:
            short = 100000000
            for person in self.persons:
                if person.height < short:
                    short = person.height
                    shortest_person = person
            return shortest_person

    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            short = self.shortest()
            self.persons.remove(short)
            return short