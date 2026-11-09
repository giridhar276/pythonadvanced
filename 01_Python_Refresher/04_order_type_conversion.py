# Example: Convert values imported from an online order form.
quantity_text = "5"
price_text = "149.75"
member_text = "yes"

quantity = int(quantity_text)
unit_price = float(price_text)
is_member = member_text.lower() == "yes"

amount = quantity * unit_price
if is_member:
    amount = amount * 0.95

print("Items ordered:", quantity)
print("Unit price:", unit_price)
print("Member discount applied:", is_member)
print("Final amount:", round(amount, 2))

# Convert the order number back to text for a label.
order_number = 2087
label = "ORDER-" + str(order_number)
print("Package label:", label)
