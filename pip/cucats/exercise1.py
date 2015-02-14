# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 23:13:00 2015

@author: Daniel
"""
from cucats.wrapper import Wrapper

def calculator(answer):
        ans = 2**1000
        return (answer == ans)

class Exercise1 (Wrapper):
    def __init__(self):
        instruction = "Use python as a calculator to calculate the value of 2^1000. Check your answer with cucats.ex1.check(answer)"
        title = "Using python as a calculator"
        Wrapper.__init__(self, title, calculator, instruction)
        print ("Exercises 1 loaded")
