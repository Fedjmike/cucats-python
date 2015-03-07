# Break a Caesar cipher - Part 2!

In our last exercise we learned how to write a function do shift a character by a certain offset. In this exercise, we will finish up our work and implement a full Caesar cipher, using list comprehensions and file handling!

## Step 1: Writing a function to shift a whole string

We have a function that we can use to shift a single character -- how can we extend that to a whole string? Remember, strings are just lists of characters! So, in order to extend our function to entire strings, all we need to do is construct a new list, where each element (i.e., character) from our initial string is shifted using our function. This is what we could use a list comprehension for! If our string is `my_string`, then a good way to iterate over all characters in it would be to do `for char in my_string`, for example. Use what we've shown you to construct a new list where each character should be replaced by having run the `shift` function on it.

Check if your function works by shifting the following sentence by 13 places:

  `Cebtenzzvat vf sha!`

## Step 2: Using a function to shift characters

Shifting a character by a number of steps seems like something we'll be doing a lot while solving ciphers. Let's write a function fo make our lives easier. From now it'll be easier to save your code in a file instead of typing it into the interpreter all the time.

* Open up your text editor of choice and write the following to `cipher.py`:

  ```python
  def shift(letter, n):
      shifted_letter = chr(ord(letter) + n)
      return(shifted_letter)
  ```

Ok, let's see if the function works:

* At the end of `cipher.py`, add

  ```python
  print(shift('r',6))
  ```

  and run `cipher.py`. You should see 'x'.
  
We're doing well, but not quite there yet.

* What happens if you do the following?

  ```python
  print(shift('y',4))
  ```

We end up getting an opening curly bracket! This is because ASCII doesn't only outline codes for the 26 alphabet - remember that there are other symbols you use (such as punctuation marks)! The problem we now need to fix is to make our program 'wrap around' the alphabet if we go beyond our ranges of 'a'-'z' or 'A'-'Z'. We can fix that using if-conditions.

## Step 3: Fixing our function to enable wrapping around

* Open up your text editor and make the following changes to `cipher.py`:  

  ```python
  def shift(letter, n):
      if letter.isupper():
          pass # Leave blank for now
      elif letter.islower():
          pass # Leave blank for now
      return(shifted_letter)
  ```
We've introduced two new functions here: `isupper()` and `islower()`. All these functions do is return `True` or `False` depending on whether or not the letter is upper case or lower case.

What is `elif`? `elif` is basically short for `else if`. Sometimes we don't just want our program to branch into two cases, there might be more we want to take care of. So, what we'd ideally like to do is run an initial test and see if it evaluates to `True`. If it does, it's all good and we can just execute the first bit of our `if-else` block. If not, there are still other cases we need to check before settling on a branch. How would we go about doing this? Run another `if-else` condition, of course! This is where an `elif` is used.

Note that `pass` just tells python 'do nothing'. Remember to remove that when you're filling in the blocks yourself!

* Modify your code to the following:

  ```python
  def shift(letter, n):
      if letter.isupper():
          if (ord(letter) + n < 65):
              pass # Leave blank for now
          elif (ord(letter) + n > 90):
              pass # Leave blank for now
          else:
              shifted_letter = chr(ord(letter) + n)
      elif letter.islower():
          if (ord(letter) + n < 97):
              pass # Leave blank for now
          elif (ord(letter) + n > 122):
              pass # Leave blank for now
          else:
              shifted_letter = chr(ord(letter) + n)
      return(shifted_letter)
  ```

Here our inner `if`-conditions here are testing if after applying the shift our letters fall in the required ranges or not (remember that 'a' is 97, 'z' is 122, 'A' is 65 and 'Z' is 90). If they don't we need to adjust them accordingly, i.e., add or subtract 26 depending on what part of the range they cross.

* Replace the blank bits of your code now with the required conditions. For example, the first of the four shoud look like:

  ```python
  shifted_letter = chr(ord(letter) + n + 26)
  ```

By having added 26 to `n`, we have successfully wrapped around the alphabet. Try the something similar on the rest!

## Step 4: Completed function

Congratulations, you're now finished with your function to perform shifts on idividual characters! This involved understanding `if`-conditions at a deeper level and using methods such as `isupper()` and `islower()` - you can now appreciate what you've done. In future sessions we'll work on extending this function to work on full sentences, so that we can decipher them with ease! Till next time!
