# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return f'{self.name} ({self.weight} kg)'
    
class Box:
    def __init__(self):
        self.presents = []
    
    def add_present(self, present: Present):
        self.presents.append(present)
    
    def total_weight(self):
        presents_weight = 0
        for present in self.presents:
            presents_weight += present.weight
        return presents_weight