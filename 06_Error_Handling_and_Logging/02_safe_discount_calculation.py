# Topic 06 - Error Handling and Logging
# Protect calculations against zero or invalid quantities.
order_cases = [(1200, 3), (500, 0), (900, 'two')]
for total, quantity in order_cases:
    try:
        per_item = total / int(quantity)
    except ZeroDivisionError:
        print('Cannot divide by zero items')
    except ValueError:
        print('Quantity must be a number')
    else:
        print('Average cost per item:', round(per_item, 2))
    finally:
        print('Order reviewed')
