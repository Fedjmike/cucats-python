# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 21:04:07 2015

@author: Daniel
"""

instruction = """


Fizz buzz is a group word game where players take turns to count incrementally, 
replacing any number divisible by three with the word "fizz", and any number 
divisible by five with the word "buzz". If a number that is both divisible by 
3 and 5, replace it with "fizzbuzz".

Your task is to write a function that takes the value n and plays the game up till and including n.
For example, if your function was named f, f(15) should print

1
2
fizz
4
buzz
fizz
...
13
14
fizzbuzz
16


"""

from cucats.wrapper import Wrapper
import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def my_inner(n):
    for i in range(1, n+1):
        if (not i % 15):
            print("fizzbuzz")
        elif (not i % 3):
            print("fizz")
        elif (not i % 5):
            print("buzz")
        else:
            print(i)

# Returns a string
def my_function(n):
    backup = sys.stdout    
    sys.stdout = StringIO()
    my_inner(n)
    out = sys.stdout.getvalue() # release output
    sys.stdout.close()  # close the stream 
    sys.stdout = backup
    return out

def check_function(f):
    # setup the environment
    N = 20
    backup = sys.stdout    
    sys.stdout = StringIO()     # capture output
    f(N)
    out = sys.stdout.getvalue() # release output
    sys.stdout.close()  # close the stream 
    sys.stdout = backup # restore original stdout
    my_out = my_function(N)
#    print(out)
#    print(my_out)
    return out == my_out

class Exercise (Wrapper):
    def __init__(self):
        title = "Fizzbuzz"
        Wrapper.__init__(self, title, check_function, instruction)
        print (title + " loaded")
