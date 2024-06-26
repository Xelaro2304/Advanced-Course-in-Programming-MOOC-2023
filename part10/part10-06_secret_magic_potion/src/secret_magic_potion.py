# Write your solution here:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")


class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        self._name = name
        self._password = password
        self._ingredients = []
    
    def __password_check (self, inputed_password):
        if self._password == inputed_password:
            pass
        else:
            raise ValueError ('Wrong password!')
    
    def add_ingredient(self, ingredient: str, amount: float, password):
        self.__password_check(password)
        return super().add_ingredient(ingredient, amount)
    
    def print_recipe(self, password):
        self.__password_check(password)
        return super().print_recipe()