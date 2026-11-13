"""
Example 07: Real-World Decorator - Measure Execution Time

Use case:
Measure how long a function takes to finish.
"""

import time


def measure_time(function):
    def wrapper():
        start = time.perf_counter()
        result = function()
        end = time.perf_counter()
        print("Execution time in seconds:", round(end - start, 4))
        return result
    return wrapper


@measure_time
def process_orders():
    print("Processing 10000 sample orders...")
    total = sum(range(10000))
    print("Processing completed. Total:", total)


process_orders()
