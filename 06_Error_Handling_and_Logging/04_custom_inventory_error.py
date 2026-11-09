# Topic 06 - Error Handling and Logging
# Raise a meaningful error for impossible stock requests.
def dispatch(available, requested):
    if requested < 1:
        raise ValueError('Request must be at least one item')
    if requested > available:
        raise ValueError('Not enough items available')
    return available - requested

for request in [3, 11, -1]:
    try:
        print('Remaining stock:', dispatch(10, request))
    except ValueError as error:
        print('Dispatch rejected:', error)
