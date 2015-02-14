# Break a Caesar cipher!

A *Caesar cipher* is a very simple encryption technique: each letter in the *plaintext* (the text to be encrypted) is replaced by a letter a fixed number of positions down the alphabet. (The output is know as *ciphertext*.) So for example `cucats` shifted left by two would give us `asayrq`. You're now going to write your very own Caesar cipher solver - let's get started!

## Step 1: Shifting characters

To shift a letter by a number of places, we need to (well, we don't *need* to, this is but one of many ways) first convert it into the corresponding ASCII number. (ASCII is just a commonly-used mapping between letters and numbers.) This can be done using the `ord` function. Go ahead, try it out:

* Launch the Python interpreter and type in:

  `ord('a')`

You should get 97, which is the ASCII code for lowercase a. Try it with uppercase 'A', what number do you get? Do you notice anything special about the difference between these numbers?

We just converted from a character to its ASCII code. To do the reverse, use the `chr` function.

* For instance, `chr(97)` should give you 'a'. Try it out.

Okay, we can convert characters to ASCII and back. Great! Now to actually shift them.

* Try converting 'a' to a number, shifting it up by 3, and then converting back to a character:

  `chr(ord('a') + 3)`

Hopefully you get 'd' back. Well done!


## Step 2: Using a function to shift characters

Shifting a character by a number of steps seems like something we'll be doing a lot while solving ciphers. Let's write a function fo make our lives easier. From now it'll be easier to save your code in a file instead of typing it into the interpreter all the time.

* Open up your text editor of choice and write the following to `cipher.py`:

  ```
  def shift(letter, n):
      shifted_letter = chr(ord(letter) + n)
      return(shifted_letter)
  ```

Ok, let's see if the function works:

* At the end of `cipher.py`, add

  ```
  print(shift('r',6))
  ```

  and run `cipher.py`. You should see 'x'.
  
We're doing good, but not quite there yet.

* What happens if you do the following?

  ```
  print(shift('y',4))
  ```

  Can you explain what's happening?

Uh oh...
