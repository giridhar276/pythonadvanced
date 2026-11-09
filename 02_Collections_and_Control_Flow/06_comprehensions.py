# Example: Prepare a small sales dashboard.
sales = [
    {"product": "Notebook", "amount": 450},
    {"product": "Bag", "amount": 1250},
    {"product": "Bottle", "amount": 300},
    {"product": "Shoes", "amount": 2100},
]

# List comprehension: sales above 500.
large_sales = [sale["product"] for sale in sales if sale["amount"] > 500]
print("Large sales:", large_sales)

# Dictionary comprehension: product to amount.
price_lookup = {sale["product"]: sale["amount"] for sale in sales}
print("Price lookup:", price_lookup)

# Set comprehension: different price bands.
bands = {"High" if sale["amount"] >= 1000 else "Low" for sale in sales}
print("Sales bands:", bands)

# Nested comprehension: combine branches and products.
branches = ["Ameerpet", "Miyapur"]
products = ["Tea", "Coffee"]
checks = [(branch, item) for branch in branches for item in products]
print("Stock check pairs:", checks)

# Filtering and transformation in one readable expression.
with_tax = [round(sale["amount"] * 1.05, 2) for sale in sales]
print("Amounts with 5% tax:", with_tax)
