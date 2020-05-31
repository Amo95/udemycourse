from collections import OrderedDict
import sys
import os


def clear():
    """clear screen"""
    os.system("cls" if os.name == "nt" else "clear")

def error(word):
    error = input("Do you need help y/N? ")

    if error in ["y", "Y"]:
        print(word)
    elif  error in ["", "N", "n"]:
        pass
    else:
        print("Wrong Entry")
        error(word)


def hangman(word):
    """Play Game"""
    clear()
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    
    rletters = list(word)
    
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter>> "
        char = input(msg)
        
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            error(word)
            
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


def helps(word):
    """Help Option"""
    return word

def quit():
    """Quit"""
    return "\n\nThanks for playing\n"
    sys.exit(1)


def begin():
    for keys, values in menus.items():
        print(f"[{keys}] {values.__doc__}")

    options = input("Select Option: ")

    if options == list(menus.keys())[0]:
        import json

        animals = json.loads(open("udemy.json").read())
        for animal in animals:
            hangman(animal)

    elif options == list(menus.keys())[1]:
        print(quit())

    else:
        print("Wrong Entry, Try again!!")
        begin()


menus = OrderedDict([
    ["p", hangman],
    ["q", quit]
    ])

if __name__ == "__main__":
    try:
        begin()
    except KeyboardInterrupt:
        print(quit())
    except EOFError:
        print(quit())