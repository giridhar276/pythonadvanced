"""
Example 03: Decorator with Return Value

Concept:
The wrapper can use and return the result of the original function.
"""


def show_result(function):
    def wrapper(a, b):
        result = function(a, b)
        print("Calculated result:", result)
        return result
    return wrapper


@show_result
def add_numbers(a, b):
    return a + b


total = add_numbers(20, 30)
print("Value returned:", total)
