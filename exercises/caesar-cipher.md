# Break a Caesar cipher!

A *Caesar cipher* is a very simple encryption technique: each letter in the *plaintext* (the text to be encrypted) is replaced by a letter a fixed number of positions down the alphabet. (The output is know as *ciphertext*.) So for example `cucats` shifted left by two would give us `ewecvu`. You're now going to write your very own Caesar cipher solver - let's get started!

## Step 1: Shifting characters

Characters in computers are internally stored as numbers, as are many other things. ASCII (American Standard Code for Information Interchange) is one character-encoding scheme that is basically a conversion scheme between characters and numbers. Each character is assigned a number. For example, the ASCII code for 'A' is 65, and the code for 'a' is 97.

To shift a letter by a number of places, we need to (well, we don't *need* to, this is but one of many ways) first convert it into the corresponding ASCII number. (ASCII is just a commonly-used mapping between letters and numbers.) This can be done using the `ord` function. Go ahead, try it out:

* Launch the Python interpreter and type in:

  `ord('a')`

You should get 97, which is the ASCII code for lowercase a. Try it with uppercase 'A', what number do you get? Do you notice anything special about the difference between these numbers? Try it with 'b', 'c' and 'd' and see if you can spot the pattern (try the uppercase versions as well!).

We just converted from a character to its ASCII code. To do the reverse, use the `chr` function.

* For instance, `chr(97)` should give you 'a'. Try it out.

Okay, we can convert characters to ASCII and back. Great! Now to actually shift them.

* Try converting 'a' to a number, shifting it up by 3, and then converting back to a character:

  `chr(ord('a') + 3)`

Hopefully you get 'd' back. Well done!


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
