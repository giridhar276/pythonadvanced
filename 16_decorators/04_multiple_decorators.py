"""
Example 04: Multiple Decorators

Concept:
More than one decorator can be applied to the same function.
The decorator closest to the function runs around it first.
"""


def first_decorator(function):
    def wrapper():
        print("Checking classroom availability")
        function()
    return wrapper


def second_decorator(function):
    def wrapper():
        print("Checking projector")
        function()
    return wrapper


@first_decorator
@second_decorator
def start_session():
    print("Session started")


start_session()
