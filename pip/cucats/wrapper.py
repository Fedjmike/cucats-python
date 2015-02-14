# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 16:35:26 2015

@author: Daniel
"""

class Wrapper:
    check_function = 1
    name = "default"
    instruction = ""
    
    def __str__(self):
        return self.instruction
        
    def print_correct(self):
        print("Correct! Well done!")

    def print_no_input(self):
        print("Please call it with cucats." + self.name + ".check(answer)")

    def print_incorrect(self):
        print("Incorrect. Please try again.")
        
    def printWrong(given_answer = None,correct_answer = None):
        if (correct_answer):
            print("Wrong!\n Expected output:", correct_answer, "\nYour output:", given_answer)
        elif (given_answer):
            print("to be implemented")
        else:
            print("Incorrect answer. Please try again.")

    def get_instruction(self):
        print(self.instruction)

    def __init__(self, name, check_function, instruction = None):
        self.name = name
        self.check_function = check_function
        self.instruction = instruction
        
    def check(self, fin=None):
        if (fin == None):
            self.print_no_input()
        elif self.check_function(fin):
            self.print_correct()
        else:
            self.print_incorrect()
