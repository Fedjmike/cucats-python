# Break a Caesar cipher!

A *Caesar cipher* is a very simple encryption technique- each letter in the *plaintext* (the text to be encrypted) is replaced by a letter a fixed number of positions down the alphabet (the output is know as *ciphertext*. So for example `cucats` shifted left by two would give us `asayrq`. You're now going to write your very own Caesar cipher solver- let's get started!

## Step one- Function to shift a character by a number of places

[Insert some stuff about how letters are stored as numbers]

To increment a letter by a number of places, we need to (well, we don't *need* to, this is but one of many ways) first convert it into the corresponding ASCII value. This can be done using the `ord` function. Go ahead, try it out:

1. Open up python and type in:

	`ord('a')`

You should get 97, which is the ASCII code for lowercase a. Try it with uppercase 'A', what number do you get? Do you notice anything special about the difference between these numbers?

2. We just converted from a character to its ASCII code. To do the reverse, use the `chr` function. For instance,
	
	`chr(97)`

should give you 'a'.

3. Okay, we can convert characters to ASCII and back. Great! Now to actually shift them. Try converting 'a' to a number, shifting it up by 3, and then converting back to a character:

	`chr(ord('a') + 3)`

Hopefully you get 'd' back. Well done!

4. **Writing a function to do this:**

Shifting a character by a number of steps seems like something we'll be doing a lot while solving ciphers. Let's write a function fo make our lives easier. From now it'll be easier to save your code in a file instead of typing it into the python interpreter all the time. Open up your text editor of choice and write the following to `cipher.py`:
```
	def shift(letter, n):
		shiftedLetter = chr(ord(letter) + n)
		return(shiftedLetter)
```
Let's take her for a spin! Type in:
	
    `print(shift('r',6))`

at the end of the file and run `cipher.py`. You should see 'x'.

5. We're doing good, but not quite there yet. What happens if you run:

	`print(shift(y,4))`

Uh oh...
