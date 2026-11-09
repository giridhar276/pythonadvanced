# Example: Manage products in a small store.
products = ["Rice", "Oil", "Soap"]
products.append("Milk")            # add at the end
products.extend(["Tea", "Sugar"])  # add multiple items
products.insert(1, "Salt")         # add at a position
print("Stock list:", products)

print("First product:", products[0])
print("Last two:", products[-2:])
print("Oil position:", products.index("Oil"))
print("Soap count:", products.count("Soap"))

products.remove("Salt")            # remove by value
sold_item = products.pop()          # remove last item
print("Sold/removed:", sold_item)

products.sort()                     # alphabetical order
print("Sorted:", products)
products.reverse()                  # reverse current order
print("Reversed:", products)

backup = products.copy()            # independent copy
backup.clear()                      # empty only the backup
print("Original products:", products)
print("Cleared backup:", backup)
