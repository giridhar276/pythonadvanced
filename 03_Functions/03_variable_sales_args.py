# Topic 03 - Functions
# *args accepts any number of sales values.
def total_sales(*amounts):
    return sum(amounts)

# **kwargs accepts named categories and their values.
def sales_by_category(**categories):
    for category, amount in categories.items():
        print(category, 'sales:', amount)
    return sum(categories.values())

print('Monday total:', total_sales(1200, 850, 600))
print('Tuesday total:', total_sales(950, 1100))
grand_total = sales_by_category(food=2300, books=900, stationery=450)
print('Category total:', grand_total)
