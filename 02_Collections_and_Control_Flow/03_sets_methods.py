# Example: Compare attendees across two training batches.
batch_a = {"Anita", "Ravi", "Meena"}
batch_b = {"Ravi", "Kiran", "Meena"}

batch_a.add("Sita")
batch_a.update(["Arun", "Divya"])
print("Batch A:", batch_a)
print("All attendees:", batch_a.union(batch_b))
print("Common attendees:", batch_a.intersection(batch_b))
print("Only in A:", batch_a.difference(batch_b))
print("Either batch but not both:", batch_a.symmetric_difference(batch_b))
print("A subset of combined:", batch_a.issubset(batch_a | batch_b))
print("Combined superset of A:", (batch_a | batch_b).issuperset(batch_a))
print("No overlap with Finance:", batch_a.isdisjoint({"Finance"}))

working = batch_a.copy()
working.intersection_update(batch_b)
print("Common (updated copy):", working)
working = batch_a.copy()
working.difference_update(batch_b)
print("A only (updated copy):", working)
working = batch_a.copy()
working.symmetric_difference_update(batch_b)
print("Unique to each (updated copy):", working)

batch_a.discard("Unknown")        # safe if missing
batch_a.remove("Arun")             # must exist
removed = batch_a.pop()            # removes an arbitrary member
print("Removed member:", removed)
print("After removals:", batch_a)
batch_a.clear()
print("After clear:", batch_a)
