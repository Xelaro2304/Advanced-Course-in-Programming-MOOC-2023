# Write your solution here:
import random
def word_generator(characters: str, length: int, amount: int):
    return ("".join(random.sample(characters, length)) for i in range (amount))
    