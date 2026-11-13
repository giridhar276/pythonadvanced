"""
Example 06: Real-World Decorator - Login Check

Use case:
Allow a user to view account information only after login.
This is a simple classroom simulation, not production authentication.
"""


def login_required(function):
    def wrapper(username, logged_in):
        if not logged_in:
            print("Access denied. Please log in first.")
            return
        return function(username, logged_in)
    return wrapper


@login_required
def view_profile(username, logged_in):
    print("Welcome to your profile,", username)


view_profile("Arjun", True)
view_profile("Priya", False)
