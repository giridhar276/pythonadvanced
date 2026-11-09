# Example: Work with fixed delivery route information.
route = ("Hyderabad", "Vijayawada", "Chennai", "Vijayawada")

print("First stop:", route[0])
print("Final stop:", route[-1])
print("Intermediate stops:", route[1:3])
print("Total stops:", len(route))
print("Vijayawada appears:", route.count("Vijayawada"), "times")
print("First Vijayawada index:", route.index("Vijayawada"))

# Packing an employee record in a tuple.
employee = (1204, "Anita", "Finance")
emp_id, emp_name, department = employee
print("Employee ID:", emp_id)
print("Employee:", emp_name)
print("Department:", department)

# Tuples are immutable. Create a new tuple to add a stop.
updated_route = route + ("Bengaluru",)
print("Updated route:", updated_route)
