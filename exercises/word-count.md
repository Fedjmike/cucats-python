# Word count challenge

You know about strings. You know that you can make a string using quotation marks. For example:
```python
my_string = "Hello! Welcome to the word count challenge. :)"
```

Because strings are commonly used, Python has some features for dealing with them.
Python knows how to split strings up into parts.
In Python, string objects have a built-in _method_ called `split`.
(A _method_ is a function which is associated with an object.)

To use a method on an object, we write the object, then a dot, then the method, then a pair of brackets, `()`, like so:
```python
my_string.split()
```
The brackets indicate that `split` is a function, rather than a variable, for instance. Functions always have brackets!


## Exercise 1

* Write a script where you make a string, and use the `print()` function to see what the result of `my_string.split()` is.
 
  Hint: it should be a list of _somethings_.

* You can also give the method an argument - something like `my_string.split("t")`. What effect does this have?


## Exercise 2

Python has a few built-in functions.
For example, we can do:
```python
>>> my_list = [1, 4, 6]
>>> sum(my_list)
11
```
Here we're using the built-in function `sum` to find the sum of the elements in the list.

* *Using the list you got in exercise 1*, use a built-in function to count the words in `my_string`. What built-in function should you use? You could use Google to help you!


## Exercise 3

You can iterate over the elements of a list - i.e. perform an action for each element.
Remember, the syntax is like this:
```python
for element in my_list:
    do_something()
```

* Can you use this to count how many times each word appears in a string? What extra data structure(s) would you need to achieve this? Have a go.
* You could start by counting how many occurences of a particular word there are, then extend this to counting all the distinct words in the string.


## Extensions

* At the moment, your program probably counts "Dog" and "dog" as different words. How could you change this?
* How can you handle punctuation? Which string methods might be helpful?
* Find out how to read a string from a text file. (Ask!)
* Find out how to write the word count results to a file. (Ask!)
* What other features would you like to add? Add them!
