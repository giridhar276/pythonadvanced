"""
Example 05: Decorator with Its Own Parameter

Concept:
Pass a value to the decorator to control its behavior.
"""


def repeat(times):
    def decorator(function):
        def wrapper():
            for number in range(times):
                function()
        return wrapper
    return decorator


@repeat(3)
def reminder():
    print("Please submit your assignment.")


reminder()
