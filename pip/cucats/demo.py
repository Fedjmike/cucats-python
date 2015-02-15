# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 20:18:19 2015

@author: Daniel
"""

from cucats.wrapper import Wrapper

def value_answer(ans):
    return ans == 42
    
def function_answer(f):
    return f() == 42

class Demo1 (Wrapper):
    def __init__(self):
        instruction = """Call the check method with the value of 40 + 2.
i.e. cucats.demo1.check(answer)"""
        title = "Demo 1"
        Wrapper.__init__(self, title, value_answer, instruction)
        print ("Demo 1 loaded")

class Demo2 (Wrapper):
    def __init__(self):
        instruction = """Write a function called f which returns the value 42.
And then call the check method with the function
i.e. cucats.demo2.check(f)"""
        title = "Demo 2"
        Wrapper.__init__(self, title, value_answer, instruction)
        print ("Demo 2 loaded")
