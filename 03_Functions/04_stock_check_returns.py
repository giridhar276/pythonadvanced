# Topic 03 - Functions
# Return multiple useful values as a tuple.
def check_stock(available, requested):
    can_deliver = requested <= available
    remaining = available - requested if can_deliver else available
    return can_deliver, remaining

stock = {'Laptop': 8, 'Mouse': 25, 'Keyboard': 12}
requests = {'Laptop': 2, 'Mouse': 30, 'Keyboard': 5}
for item, requested in requests.items():
    approved, balance = check_stock(stock[item], requested)
    if approved:
        stock[item] = balance
        print(item, 'Approved. Remaining:', balance)
    else:
        print(item, 'Insufficient stock')
