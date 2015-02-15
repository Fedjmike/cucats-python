# Data structure and classes 

* Learn about list, tuples, dictionary
* Understand shared references
* Making your own data structure (classes)

Learn about a useful type called dictionary in python and how to use it.An analagy for dictionary is a telephone book. We want to be able to store the telephone number (value) of someone (key) and be able to look it up again later.

List is just a collection of **ordered** orjects. Learn more about lists and what we can use it for.

Tuples are like list, but you can't change it. Think of making a list as writing something down on a paper with ink. If you want to change the content, you need to start with another paper.

__Shared references__ 

Variables are labels, a single object can have multiple labels. What if the we change the object by referring it with one of the labels?

__Own data structure__

The basic types mentioned above may not be sufficient to represent your object. Imagine if we want to introduce the concept of a car, or a human being, how can we represent it in Python?


## List

List is just a collection of **ordered** orjects. You can get the methods of a list object, e.g. x, with dir(x)

* Multiple types [1, "elephant", x]
* len, append, insert, remove, slicing, sort

## Tuples

Tuples are like lists, but immutable, which means that you can't modify it after you have created it.

## Dictionary

Dictionary is a mapping of key value pairs. Back to the phone book example. We can create a phone book with the name of the people as keys, and information such as their phone numbers as the values.

* Give an eg
* how to look up, update

## Shared references

* What happens if you do 
    
    x = [1,2,3]
    y = x
    y[1] = 10
    print(x)

* When do we need to worry about this?

## Classes

* Why do we want to use this
* Demonstrate a car class

# Summary

* When do we use the different types and why?

