# Topic 04 - Modules and Project Basics
import statistics
# Summarize daily visitor counts from a small store.
visitors = [42, 55, 48, 60, 55, 39, 51]
print('Average visitors:', round(statistics.mean(visitors), 1))
print('Median visitors:', statistics.median(visitors))
print('Most common count:', statistics.mode(visitors))
print('Lowest count:', min(visitors))
print('Highest count:', max(visitors))
