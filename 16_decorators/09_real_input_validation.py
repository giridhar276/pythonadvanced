"""
Example 09: Real-World Decorator - Validate Amount

Use case:
Prevent a payment function from accepting zero or negative amounts.
"""


def validate_amount(function):
    def wrapper(amount):
        if amount <= 0:
            print("Invalid payment amount:", amount)
            return
        return function(amount)
    return wrapper


@validate_amount
def make_payment(amount):
    print("Payment of", amount, "processed successfully.")


make_payment(1500)
make_payment(-100)
