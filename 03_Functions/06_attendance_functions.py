# Topic 03 - Functions
# Small reusable functions for a training attendance report.
def attendance_percent(present, total):
    if total == 0:
        return 0
    return round(present / total * 100, 1)

def attendance_status(percent, minimum=75):
    return 'Eligible' if percent >= minimum else 'Short attendance'

students = {'Asha': (18, 20), 'Ravi': (14, 20), 'Kiran': (20, 20)}
for name, days in students.items():
    percent = attendance_percent(days[0], days[1])
    status = attendance_status(percent)
    print(name, percent, 'percent:', status)
