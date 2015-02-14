<!-- MarkdownTOC depth=6 bracket=round autolink=true -->

- [Getting cucats python exercise package](#getting-cucats-python-exercise-package)
    - [Getting the package](#getting-the-package)
    - [Using the package](#using-the-package)
        - [Listing the exercises available](#listing-the-exercises-available)
        - [Demo 1: Submitting a value](#demo-1-submitting-a-value)
        - [Demo 2: Submitting a function](#demo-2-submitting-a-function)

<!-- /MarkdownTOC -->

# Getting cucats python exercise package

## Getting the package

Open the terminal/command prompt and enter 
`pip install --user http://cucats.org/python-package`

## Using the package

Run python, enter `import cucats`.
This will load the module with the exercises we have prepared.

### Listing the exercises available
`cucats.exercises`
Here we can see the list of exercises available.

    >>> cucats.exercises
    ['ex1', 'ex2', 'demo1', 'demo2']  

Our exercises will ask you to provide either a value or implement a function. The demo below will walk you through how to do both.

### Demo 1: Submitting a value
To get the instruction of the demo exercise 1. Enter
`cucats.demo1.get_instruction()`
You should see 
 
    >>> cucats.demo1.get_instruction()
    Call the check method with the value of 40 + 2.
    i.e. cucats.demo1.check(answer)

We know 40 + 2 = 42. So we check out answer with
`cucats.demo1.check(42)`

    >>> cucats.demo1.check(42)            
    Correct! Well done!

What if we made a mistake?
`cucats.demo1.check(41)`

    >>> cucats.demo1.check(41)   
    Incorrect. Please try again. 

If we store our value as a variable like `x = 40 + 2`, then we can submit it with 

    >>> x = 40 + 2
    >>> cucats.demo1.check(x)
    Correct! Well done!


### Demo 2: Submitting a function
This demo will show you how to check your answer if the exercise is for you to implement a function.

We first get instruction by typing 
`cucats.demo2.get_instruction()`

    >>> cucats.demo2.get_instruction()
    Write a function called f which returns the value 42.
    And then call the check method with the function
    i.e. cucats.demo2.check(f)

So we start by defining a function to do that:

    def test():
        return 42

and then we can submit our function with

    >>> cucats.demo2.check(test)   
    Correct! Well done!