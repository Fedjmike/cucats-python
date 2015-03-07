# Break a Caesar cipher - Part 2!

In our last exercise we learned how to write a function do shift a character by a certain offset. In this exercise, we will finish up our work and implement a full Caesar cipher, using list comprehensions and ranges.

This exercise will involve more coding on your own, but once you're done you should be able to appreciate the concepts that you've managed to learn (and make use of)!

## Step 1: Writing a function to shift a whole string

We have a function that we can use to shift a single character -- how can we extend that to a whole string? Remember, strings are just lists of characters! So, in order to extend our function to entire strings, all we need to do is construct a new list, where each element (i.e., character) from our initial string is shifted using our function. This is what we could use a list comprehension for! If our string is `my_string`, then a good way to iterate over all characters in it would be to do `for char in my_string`, for example. Use what we've shown you to construct a new list where each character should be replaced by having run the `shift` function on it.

Check if your function works by deciphering the following sentence by shifting it 13 places:

  `Cebtenzzvatvfsha`

If you've done everything correctly you'll now see a list of characters, which is good, but not the best we can do. What we need is a string, so we can convert that list of characters to a string by running

  `''.join(new_string)`

where `new_string` is the list of characters you got after having used the list comprehension. Everything should look correct now.

## Step 2: Fixing our function

You might have noticed I ommitted the spaces in the previous example. This is actually because our function stops working if we use it! Go ahead an try it out on a sentence with spaces, and see what error you get. This happens because in our code we essentially have two branches to execute -- one if the letter is upper case and the other if it is lower case.

What about a space, or any other special character for that matter? Are they upper or lower? The answer is that they're neither! We should always account for such inputs, so we need to make a minor modification to our `shift` function. Here it is from last time:

  ```python
  def shift(letter, n):
      if letter.isupper():
          # Do some things
      elif letter.islower():
          # Do some other things
      return(shifted_letter)
  ```

The problem we have is that if we have non alphabetic characters, the interpreter immediately goes to the last line, which returns the `shifted_letter`. But we haven't initialised it, and so python complains! What we should do is have a final backup, in case the first two cases fail. This can be done by having a final `else` statement, that will set the value of `shifted_letter` accordingly (what should its value be if it is neither upper nor lower case?).

Finally, your `shift` function should look like:

  ```python
  def shift(letter, n):
      if letter.isupper():
          # Do some things
      elif letter.islower():
          # Do some other things
      else:
          # What goes here? We need to
          # initialise shifted_letter
      return(shifted_letter)
  ```
You should now be able to retry your list comprehension, but on the following sentence and see if it works:

  `Cebtenzzvat vf sha!`

## Step 3: Trying all possible combinations 

It's good that we can shift a string given the amount of places we have to shift each character by, but what if we didn't know that information? There are interesting and fast approaches that professional cryptographers use, but let's try something more naive. Let's try shifting the sentence by all the numbers we can shift it by (so from 1 to 25), and just read the new sentences to see which one is actually readable.

Remember, we want to iterate the same piece of code here while only changing one value, which is the amount we want to shift our letters by. Such a task is perfect for a `for` loop. We need our loop to range over the integer values from 1 to 25 inclusive. We can do this by using range! Try the following:

  ```python
  for num in range(1,26):
      print(num)
  ```

We get the numbers we want! You should now modify your loop to run the list comprehension based on the value of `num`, and then print out the resulting string. Everything should be inside the `for` block. See if you can decipher the following sentences:

`Z cfmv TLTrKJ reu kyvzi gifxirddzex nfibjyfgj!`

`Oz'y kgyokx zu gyq luxmobktkyy zngt oz oy zu mkz vkxsoyyout.`


## Step 4: Completed function!

Now that you have working code, you might want to polish it up a bit, document parts that you feel are important for your understanding, and so on. Your final task is to wrap up all of your code as a function, which when given a string should be able to output all the different possible deciphered pieces of text so you can read them all and pick out the most correct one! It should look like this:

  ```python
  def decipher(encrypted_text):
      # Here's your main for loop that should
      # iterate over all required integer values

      #    Use the list comprehension method to
      #    return a list of shifted characters

      #    Join this list to convert it to a
      #    string

      #    Print out your string!
  ```

