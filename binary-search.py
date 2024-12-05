#!/usr/bin/env python3
import sys

input_guess_string = sys.argv[1]
my_list = [1, 3, 5, 7, 9]
numbers_through_100 = list(range(0, 101))

def test_binary_search():
    assert binary_search(my_list, 3) == 1
    assert binary_search(my_list, -1) == None

def test_my_binary_search_with_my_numbers():
    assert my_binary_search(numbers_through_100, 50) == (50, 1, [50])

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
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

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




if __name__ == "__main__":
    try:
        input_guess = int(input_guess_string)
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)

    # result = my_binary_search(numbers_through_100, input_guess)
    result = my_binary_search(numbers_through_100, input_guess)
    if result == None:
        print("Number is not in the array")
    else:
        array_index = result[0]
        number_of_guesses = result[1]
        guesses = result[2]
        print(f"We guessed the following numbers {guesses}")
        print(f"The index is {array_index} and was found with {number_of_guesses} guesses")
