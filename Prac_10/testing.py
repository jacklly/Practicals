"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return (" ").join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # DONE: 2. write assert statements to show if Car sets the fuel correctly
    test_car = Car()
    assert test_car.name == ""
    assert test_car._odometer == 0
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    phrased_to_sentence("how now brown cow")
    phrased_to_sentence("How now brown cow.")


# DONE: 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# DONE: 4. Fix the failing is_long_word function

def phrased_to_sentence(phrase=""):
    sentence = phrase.capitalize()
    if sentence[-1] != ".":
        sentence += ","
    return sentence


run_tests()
