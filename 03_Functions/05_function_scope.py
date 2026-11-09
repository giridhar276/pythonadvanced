# Topic 03 - Functions
# Local variables live inside functions; shared data is passed in.
tax_rate = 0.05
def invoice_total(amount, tax):
    tax_amount = amount * tax
    total = amount + tax_amount
    return total

orders = [500, 1200, 900]
for amount in orders:
    print('Order:', amount, 'Invoice:', invoice_total(amount, tax_rate))

# A different rate does not change the shared tax_rate.
special_rate = 0.02
print('Special invoice:', invoice_total(1200, special_rate))
print('Normal tax rate:', tax_rate)
