#Hi guys, this is the hang man SUPER GAME
from classFile import Hangman as hg


def load_words(filename):
    with open("words.txt", "r") as file:
        words=[line.strip() for line in file if line.strip()] # Check later
    return words

word_list=load_words("words.txt")

game = hg(word_list)

while not game.is_won() and not game.is_lost() :
    user_guess =  input("have a try: ")
    if game.is_used(user_guess):
        print("Already used")
        continue
    if game.is_in_word(user_guess): 
            game.add_char(user_guess)
            print("well done!")
    else:
        game.lost_attempt()
        game.show_hangMan()
        print("Wrong")

    game.display_word()
    game.display_totalAttemps() 
    
if game.is_won():
    print("You won")
else:
    print("You lost")   


"""1️⃣ Prevent losing attempts on repeated letters
2️⃣ Show remaining attempts
3️⃣ Full hangman drawing
4️⃣ Multiple guesses at once
5️⃣ Word list from a file
6️⃣ Turn this into a class
7️⃣ Convert it to a terminal game (colors, clear screen)
"""
    