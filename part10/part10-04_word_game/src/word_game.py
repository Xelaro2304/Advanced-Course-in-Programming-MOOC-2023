# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
           return 3


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels =['a','e','i','o','u']
        p1_vowels = 0
        p2_vowels = 0
        for vowel in vowels:
            p1_vowels += player1_word.count(vowel)
            p2_vowels += player2_word.count(vowel)
        if p1_vowels > p2_vowels:
            return 1
        elif p1_vowels < p2_vowels:
            return 2
        else:
            return 3

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    
    def round_winner(self, player1_word: str, player2_word: str):
        options = 'rock paper scissors'
        if player1_word in options and player2_word in options:
            if player1_word == 'rock' and player2_word == 'scissors':
                return 1
            elif player1_word == 'rock' and player2_word == 'paper':
                return 2
            elif player1_word == 'paper' and player2_word == 'rock':
                return 1
            elif player1_word == 'paper' and player2_word == 'scissors':
                return 2
            elif player1_word == 'scissors' and player2_word == 'paper':
                return 1
            elif player1_word == 'scissors' and player2_word == 'rock':
                return 2
            else:
                return 3
        elif player1_word in options:
            return 1
        elif player2_word in options:
            return 2
        else:
            return 3
  