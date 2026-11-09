# Topic 03 - Functions
# Reusable functions avoid repeating salary calculations.
def monthly_pay(days_worked, daily_rate):
    return days_worked * daily_rate

def salary_after_bonus(salary, bonus_percent):
    bonus = salary * bonus_percent / 100
    return salary + bonus

employees = {'Anita': 22, 'Ravi': 20, 'Meena': 24}
for name, days in employees.items():
    basic = monthly_pay(days, 1200)
    total = salary_after_bonus(basic, 5)
    print(name, 'Basic:', basic, 'Total:', round(total, 2))
