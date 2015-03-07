## Ex 2.1 Aliasing (Values and variables)
Write a function `add_one` that takes a list and adds the value `1` at the end.

```py
>>> myList = ['a']
>>> add_one(myList)
>>> myList
['a',1]
```

## Ex 2.2 Palindrome testing (Slicing)
A very useful idiom for reversing a string `s` is to do `s[::-1]`. Write a function `is_palindrome` that checks if a given string or number is a palindrome. 

A palindrome is a phrase or number that reads the same forward and backwards.
The following are examples of palindrome:

* Was it a car or a cat I saw?
* A nut for a jar of tuna.
* Do geese see God?

For the purpose of this exercise, we can assume there are no whitespaces in the input, and we care about character cases.

```py
>>> is_palindrome(12321)
True
>>> is_palindrome(122)
False
>>> is_palindrome("radar")
True
>>> is_palindrome("Kayak")
False
```

If you're keen, modify is_palindrome such that it takes as input a phrase with spaces and is case insensitive.

Hint: `s.replace(a,b)` returns a copy of the string with all occurrences of a in s replaced by b. `s.lower()` returns a copy of the string with all the cased characters converted to lowercase.


## Ex 2.3 Odd position phrases (Slicing)

Write a function `odd_words` that takes a phrase and returns a new phrase with only the odd words

```py
>>> odd_words("Tom only has two apples.")
Tom has apples.
```

Hint: You can use `s.split()` to get a list of words in s separated by whitespace and `" ".join(myList)` to join words in a list by adding a whitespace between elements of the list.

## Ex 2.4 Simple score board (Dictionary)
In this exercise, we're going to try and create a scoreboard for players. The key is going to be their name, while the value is their score.
Create an empty dictionary and write functions that does the following:

* add_player - Adds a player into the dictionary with score 0
* increment_score(name, value) - increment `name`'s score by value. If name is not in the scoreboard, print an error.
* remove_player - Removes a player
* add_score_to_all(x): increment every player's score by x
* get_players: returns a list of players.

```py
>>> score_board = {}
>>> add_player("Dan")
>>> score_board
{"Dan":0}
>>> increment_score("Dan",100)
>>> score_board
{"Dan":100}
>>> increment_score("John",100)
Unknown player John
>>> add_player("John")
>>> remove_player("Dan")
>>> score_board
{"John":0}
```

## Ex 2.5 Number guessing game (input, while)
Here we're going to create a number guessing game. We will randomly choose a number, and ask the user to guess the number. If the user guesses the number correctly, the program exits. Otherwise it says whether the number is higher or lower.

we can get a random number by using the random module. The `random.random()` function returns a random decimal between 0 and 1, including 0.

```py
from random import random
# To generate a random number from 0 to 99, 
random_number = int(100*random())
```

Expected behaviour

~~~txt
Please enter a number
5
The number I have chosen is higher.
Please enter a number
7
The number I have chosen is lower.
Please enter a number
6
Correct!
~~~

### Extension

* Output the number of tries before getting the answer as well.

## Ex 2.6 Number of words in Pride and Prejudice (file)

* Download the book [here](http://www.gutenberg.org/cache/epub/1342/pg1342.txt) and save it to the same directory as your working folder.
* Open the file and count the number of words. [You should get 124588]

Extension: 

* Count the number of occurrences of "Bennet". You should get 333 if you include occurrences like "Bennet's", "Bennets", "BENNET" etc.

Hint: Use `s.startswith(x)` to check if a string s starts with x