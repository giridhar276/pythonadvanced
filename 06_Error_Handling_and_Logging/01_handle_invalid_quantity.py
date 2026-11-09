# Topic 06 - Error Handling and Logging
# A customer might enter text or a negative quantity.
values = ['5', 'abc', '-2', '8']
for value in values:
    try:
        quantity = int(value)
        if quantity <= 0:
            raise ValueError('Quantity must be positive')
        print('Accepted quantity:', quantity)
    except ValueError as error:
        print('Invalid input:', value, '-', error)
