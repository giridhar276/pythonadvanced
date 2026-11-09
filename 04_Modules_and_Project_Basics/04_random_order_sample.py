# Topic 04 - Modules and Project Basics
import random
# Use a fixed seed so trainees see the same demonstration.
orders = ['ORD101', 'ORD102', 'ORD103', 'ORD104', 'ORD105']
random.seed(21)
selected = random.sample(orders, 2)
queue = orders.copy()
random.shuffle(queue)
print('Orders selected for review:', selected)
print('Random processing order:', queue)
print('Random sample order:', random.choice(orders))
