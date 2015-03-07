# Solution for 2.1

def add_one(x):
    x.append(1)

# Solution for 2.2

def is_palindrome(x):
    t = str(x)
    return t[::-1] == t

def is_palindrome(x):
    t = str(x).replace(" ","").lower()
    return t[::-1] == t

# Solution for 2.3 

def odd_words(x):
    return "".join(x.split()[::2])

# Solution for 2.4

def add_player(x):
    score_board.update({x:0})

def increment_score(x,y):
    if not score_board.has_key(x):
        print ("Unknown player " + x)
    else:
        score_board[x] = score_board[x] + y
    # Lazy to do the rest.

# Solution for 2.5

def run_solution25():
    from random import random
    random_number = int(100*random())
    while True:
        guess = int(input("Please enter a number between 0 and 99 inclusive: "))
        if guess == random_number:
            print("Correct!")
            return
        elif guess < random_number:
            print("The number I have chosen is higher.")
        else:
            print("The number I have chosen is lower.")

# Solution for 2.6


def run_solution26():
    import string
    counter = 0
    # Not necessary unless you want to find exact matches for Bennet and want to exclude Bennet's
    # a = string.maketrans(string.punctuation," "*len(string.punctuation)) 
    with open("book.txt") as file:
        b = file.read()
        for word in b.split():
            # Use this if you want to include "BENNET"
            # if word.lower().startswith("bennet"):
            if word.startswith("Bennet"):
                counter = counter + 1
    print(counter)