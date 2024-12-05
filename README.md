## Guess my number 

If I play a guessing game with you where you have to guess the number I'm thinking of between 0 and 100, and after each guess I tell you if the number is higher or lower, what's the best strategy?

Let's first talk about what's likely the worst strategy.  The worst strategy is:

You: 1

Me: Higher

You: 2

Me: Higher

You: 3

It's apparent without much thought that this could take _up to_ 101 guesses, and it is generally just a bad strategy.  Even if my number is 1, it's, generally speaking, a bad strategy.

## The best strategy

This may not be as apparent straight off the top of your head, but the best strategy is the following.

You: 50

Me: Higher

You: 75

Me: Lower

You: 62

Me: Higher

You: 68

Me: You got it!

It's just apparent that if you keep cutting the remaining numbers in half and guessing the middle number, you're throwing away the largest amount of numbers you can each guess, until you get down to so few remaining number, you have but 1, or stumble upon the correct one on the way to that last standing number.

## Let's code it, tests first.

```python
my_list = [1, 3, 5, 7, 9]

def test_binary_search():
    assert binary_search(my_list, 3) == 1
    assert binary_search(my_list, -1) == None
```

We want to make a function `binary_search` that satisfies those tests.  Give the function a number, and it tells you the array index.  Give the function the number `3` and it tells you it's array index is `1`. Give it `-1` which doesn't exist, it gives you `None`.

## Binary search function

```python
def binary_search(arr,item):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None
```

This function is pretty self-explanatory.  Give it an array, give it an `item`, which is what it looks for, and it will spit out the array index, using the _algorithm_ described earlier.  This function and idea were taken from the book [Grokking Algorithms](https://www.manning.com/books/grokking-algorithms).  In fact, I'll be using this to _grok algorithms_ amazingly enough, so I'll be citing this book a lot in future writings.


## Let's spice it up
I want more information, I don't just want the index, I want how many guesses and which guesses were made.  When I made that guessing game example at the top of this writing, I just halved the difference and added or subtracted from or to the lower number or higher number.  Is that really _exactly_ what's going on?

I'm terribly afraid of things like the [fencepost error](https://en.wikipedia.org/wiki/Off-by-one_error#Fencepost_error) and casually rounding and other such errors when doing rote Math off the top of my head.  Let's make the computer do the rote math.

### Learning some new Python tricks

First off, I sure as heck don't want to write an array with `[0, 1, 2, 3, ... 100]`.  I don't want to type out 100 numbers.  That's madness.  Computer do it for me!

```python
numbers_through_100 = list(range(0, 101))
```

The ole' LLM machine tells me that's how you do it.  To me it reads a little clunky because the list doesn't really include the 101, but I'm gonna leave dogs lying down and all that.

Apparently in Python, they call arrays lists, or really there is something called an array, but it's part of a module or something.  I'm just gonna call these collections arrays.  And probably lists sometimes.  Enjoy.

### My function

First things first, I want to see how many guesses my algorithm takes.  It's easy enough to add.

```python
def my_binary_search(arr,item):
    low = 0
    high = len(arr)-1
    guesses = 0

    while low <= high:
        guesses += 1
        mid = (low + high) // 2
        guess = arr[mid]
        ...
```

And, of course the test to go along with it.

```python
def test_my_binary_search():
    assert my_binary_search(numbers_through_100, 50) == (50, 1)
```

### Now what are the guesses? 

I've expanded upon the function to be able see how many guesses it takes to find the index, but I'd also like to see _what_ guesses the algorithm makes before it gets to its answer.  I'd like to see if the guessing game example at the top of this writing made sense!  I did it right off the top of my head, so maybe it doesn't! 

_let's find out_

First sauce up our testarooney

```python
def test_my_binary_search_with_my_numbers():
    assert my_binary_search(numbers_through_100, 50) == (50, 1, [50])
```

I realized my naming convention of calling the _number of guesses_ just plain _guesses_ really threw a wrench in my hammer.  I updated it to a better name and added a variable which is more appropriately called `guesses`

```python
def my_binary_search(arr,item):
    low = 0
    high = len(arr)-1
    list_of_guesses = []
    number_of_guesses = 0

    while low <= high:
        number_of_guesses += 1
        mid = (low + high) // 2
        list_of_guesses.append(mid)
        guess = arr[mid]

        if guess == item:
            return (mid, number_of_guesses, list_of_guesses)
        ...
```

### Final thoughts

So my initial example at the top was _correct_.  Is this because I'm a genius?  Well, head size is correlated to intelligence and I'm basically an Easter Island statute, so I'll let you put too and too together. 

[Github Repo](https://github.com/whynom/python-binary-search-beginning-algorithm) with all the finalized code.
