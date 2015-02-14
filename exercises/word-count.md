# Word count challenge

You know about strings. You know that you can make a string using quotes. For example:
```
my_string = "Hello! Welcome to the word count challenge. :)"
```

Because strings are commonly used, Python has some built-in features for dealing with them.
Python knows how to split string objects up into parts.
In Python, string objects have a built-in _method_ called `split`.
(A _method_ is a function associated with an object.)

To use a method on an object, we write the object, then a dot, then the method, then a pair of brackets, `()`, like so:
```
my_string.split()
```
The brackets indicate that `split` is a function, rather than a variable, for instance. Functions always have brackets!


## Exercise 1

* Use IDLE, or the `print()` function, to see what `my_string.split()` is.
 
  Hint: it should be a list of _somethings_.

* You can also give the method an argument - something like `my_string.split("t")`. What effect does this have?


## Exercise 2

Lists have methods too. You can use a method on the list you got in exercise 1 to count the words in `my_string`.

* What method should you use? You could use Google to help you!


## Exercise 3

You can iterate over the elements of a list - i.e. perform an action for each element.
Remember, the syntax is like this:
```
for element in my_list:
    do_something()
```

* Can you use this to count how many times each word appears in a string? What extra data structures would you need to achieve this? Have a go.
* You could start by counting how many occurences of a particular word there are, then extend this to counting all the distinct words in the string.


## Extension

* How can you handle punctuation?

There are many ways you could attempt this.

Hint: you can iterate over the characters in a string, just like elements in a list.
