# Example: Prepare a gym renewal summary.
member_name = "Rahul"
monthly_fee = 1800
months = 3
trainer_required = True
trainer_fee_per_month = 700

membership_cost = monthly_fee * months
trainer_cost = 0
if trainer_required:
    trainer_cost = trainer_fee_per_month * months

subtotal = membership_cost + trainer_cost
loyalty_discount = 200 if months >= 3 else 0
total = subtotal - loyalty_discount

print("Member:", member_name)
print("Duration in months:", months)
print("Membership cost:", membership_cost)
print("Trainer cost:", trainer_cost)
print("Loyalty discount:", loyalty_discount)
print("Final amount:", total)
print("Renewal approved:", total > 0)
