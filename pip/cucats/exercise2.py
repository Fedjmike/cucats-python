# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 19:26:35 2015

@author: Daniel
"""
from random import random as rand
from cucats.wrapper import Wrapper

def squaring(f):
    test = [int(rand()*1000) for i in range(100)]
    answer = [x*x for x in test]
    user_answer = [f(x) for x in test]
    if (answer == user_answer):
        Wrapper.printCorrect()
    else:
        Wrapper.printWrong(user_answer, answer)

class Exercise2 (Wrapper):
    def __init__(self):
        instruction = "Write a function f that returns the square of the input. Call ex2.check(f)"
        title = "Writing a "
        Wrapper.__init__(self, title, squaring, instruction)
        print ("Exercises 2 loaded")
