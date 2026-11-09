# Example: Register a participant for a Python workshop.
# Sample inputs: Ravi, 2, 1200
name = input("Participant name: ").strip().title()
seats = int(input("Number of seats: "))
price = float(input("Fee per seat: "))

if seats <= 0 or price < 0:
    print("Enter valid seats and fee.")
else:
    total = seats * price
    print("Registration summary")
    print("Participant:", name)
    print("Seats:", seats)
    print("Fee per seat:", price)
    print("Total payable:", round(total, 2))
    print("Registration received successfully.")
