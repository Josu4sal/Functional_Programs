import random

class Hangman:
    def __init__(self, words):
        self.word = random.choice(words)
        self.visible = ["_"] * len(self.word)
        self.used = set()
        self.totalAttempts = len(self.word) + 2

     
    def is_in_word(self, char):
        return char in self.word
           
    def is_used(self, char):
        if char in self.used:
             return True
        else:
            self.used.add(char)
            return False
        
    def add_char(self, char):
        for index, c in enumerate(self.word):
            if c == char:
                 self.visible[index] = char 
              
    def show_hangMan(self):
        graphics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

     
        max_draws = len(graphics) - 1
        index = max_draws - self.totalAttempts
        index = max(0, index)
        print(graphics[index], "   ", index, "   ", self.totalAttempts, "   ", max_draws)


    def display_word(self): 
        print("".join(self.visible))

    def display_totalAttemps(self):
        print(f"Total attempts left: {self.totalAttempts}" )

    def lost_attempt(self):
        self.totalAttempts -= 1

    def is_won(self):
            return "_" not in self.visible

    def is_lost(self):
            return self.totalAttempts == 0 and "_"  in self.visible