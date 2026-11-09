# Topic 04 - Modules and Project Basics
import math
# Boxes must be whole numbers, so round the required count up.
items = 77
items_per_box = 12
boxes = math.ceil(items / items_per_box)
empty_slots = boxes * items_per_box - items
print('Items:', items)
print('Boxes to order:', boxes)
print('Empty slots:', empty_slots)
print('Square root of 144:', math.sqrt(144))
