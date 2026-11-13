"""
Example 02: Decorator with Function Arguments

Concept:
The wrapper receives and forwards arguments to the original function.
"""


def show_details(function):
    def wrapper(name, course):
        print("Registration details:")
        function(name, course)
    return wrapper


@show_details
def register_student(name, course):
    print("Student:", name)
    print("Course:", course)


register_student("Arjun", "Python")
