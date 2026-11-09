# Topic 03 - Functions
# Default and keyword arguments make orders flexible.
def delivery_bill(amount, distance_km=3, free_above=1000):
    if amount >= free_above:
        delivery_charge = 0
    else:
        delivery_charge = distance_km * 10
    return amount + delivery_charge

local_order = delivery_bill(700)
distant_order = delivery_bill(700, distance_km=8)
premium_order = delivery_bill(amount=1500, free_above=1200)
print('Local delivery:', local_order)
print('Distant delivery:', distant_order)
print('Premium order:', premium_order)
