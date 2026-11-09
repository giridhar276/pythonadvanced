# Example: Maintain a customer order record.
order = {"id": 1007, "customer": "Ravi", "status": "New"}
print("Order ID:", order.get("id"))
print("Courier:", order.get("courier", "Not assigned"))
print("Fields:", list(order.keys()))
print("Values:", list(order.values()))
print("Field/value pairs:", list(order.items()))

order.update({"status": "Packed", "city": "Hyderabad"})
order.setdefault("payment", "Pending")
order.setdefault("payment", "Paid")  # existing value stays
print("Updated order:", order)

removed_city = order.pop("city")
print("Removed city:", removed_city)
last_pair = order.popitem()        # removes most recently inserted pair
print("Removed last pair:", last_pair)

backup = order.copy()
backup.clear()
print("Original order:", order)
print("Empty backup:", backup)

fields = ["name", "phone", "email"]
registration = dict.fromkeys(fields, "Not provided")
print("New registration:", registration)
