# Example: Calculate a bill for a stationery shop.
notebooks = 4
notebook_price = 65
pens = 3
pen_price = 20
discount_percent = 10

subtotal = notebooks * notebook_price + pens * pen_price
discount = subtotal * discount_percent / 100
final_amount = subtotal - discount

print("Notebooks total:", notebooks * notebook_price)
print("Pens total:", pens * pen_price)
print("Subtotal:", subtotal)
print("Discount:", round(discount, 2))
print("Amount to pay:", round(final_amount, 2))

paid = 300
print("Customer paid:", paid)
print("Balance or change:", round(paid - final_amount, 2))
