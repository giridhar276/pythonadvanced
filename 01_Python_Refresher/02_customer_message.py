# Example: Clean customer details before sending a message.
customer = "  priya sharma  "
city = "hyderabad"
order_code = "ORD-2026-104"

clean_name = customer.strip().title()
city_name = city.capitalize()
print("Customer:", clean_name)
print("City:", city_name)
print("Order:", order_code)

print("First name:", clean_name.split()[0])
print("Order number:", order_code.split("-")[-1])
print("Valid order prefix:", order_code.startswith("ORD"))
print("Customer contains 'Sharma':", "Sharma" in clean_name)

message = "Hello NAME, your order ORDER is confirmed."
message = message.replace("NAME", clean_name)
message = message.replace("ORDER", order_code)
print("Message:", message)
