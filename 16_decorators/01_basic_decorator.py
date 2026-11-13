"""
Example 01: Basic Decorator

Concept:
A decorator adds extra functionality before or after a function.
"""


def welcome_message(function):
    def wrapper():
        print("Welcome to Python training!")
        function()
        print("Thank you for joining.")
    return wrapper


@welcome_message
def start_class():
    print("Today's topic is decorators.")


start_class()
