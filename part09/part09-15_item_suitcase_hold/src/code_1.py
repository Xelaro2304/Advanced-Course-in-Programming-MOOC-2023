# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f'{self.name()} ({self.weight()} kg)'
    

    def weight(self):
        return self.__weight
    
   
    def name(self):
        return self.__name
    
class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.items = []
    
    def add_item(self, item):
        total_weight = self.weight()
        if total_weight + item.weight() < self.max_weight:
            self.items.append(item)

    def weight(self):
        total_weight = 0
        if self.items == []:
            return total_weight
        else:
            for item in self.items:
                total_weight += item.weight()
            return total_weight
    
    def __str__(self):
        total_items = len(self.items)
        if total_items != 1:
           return f'{total_items} items ({self.weight()} kg)'
        else:
            return f'{total_items} item ({self.weight()} kg)'
        
    def print_items(self):
        for item in self.items:
            print(item)
    
    def heaviest_item(self):
        if self.items == []:
            return None
        else:
            heaviest = 0
            for item in self.items:
                if heaviest < item.weight():
                    heaviest = item.weight()
                    heaviest_item = item
            return heaviest_item
        
class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.cargo = []
    
    def add_suitcase(self, suitcase):
        total_weight = self.weight()
        if total_weight + suitcase.weight() < self.max_weight:
            self.cargo.append(suitcase)
    
    def __str__(self):
        total_items = len(self.cargo)
        weight_left = self.max_weight - self.weight()
        if total_items != 1:
            return f'{len(self.cargo)} suitcases, space for {weight_left} kg'
        else:
            return f'{len(self.cargo)} suitcase, space for {weight_left} kg'

    def weight(self):
        total_weight = 0
        if self.cargo == []:
            return total_weight
        else:
            for cargo in self.cargo:
                total_weight += cargo.weight()
            return total_weight
    
    def print_items(self):
        for cargo in self.cargo:
            cargo.print_items()
