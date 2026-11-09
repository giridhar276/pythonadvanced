# Example: Decide which store orders qualify for free shipping.
orders = [
    {"customer": "Anita", "amount": 1500, "paid": True},
    {"customer": "Ravi", "amount": 450, "paid": True},
    {"customer": "Meena", "amount": 2100, "paid": False},
    {"customer": "Kiran", "amount": 950, "paid": True},
]

for number, order in enumerate(orders, start=1):
    if not order["paid"]:
        print(number, order["customer"], "- payment pending")
        continue
    elif order["amount"] >= 1000:
        print(number, order["customer"], "- free delivery")
    else:
        print(number, order["customer"], "- delivery charge applies")

# A small stock check using while and break.
stock = ["Milk", "Tea", "Rice", "Oil"]
position = 0
while position < len(stock):
    if stock[position] == "Rice":
        print("Rice found at shelf position:", position + 1)
        break
    position += 1

# Nested loops: two locations and two products.
for branch in ["North", "South"]:
    for product in ["Milk", "Tea"]:
        print("Stock check:", branch, product)
