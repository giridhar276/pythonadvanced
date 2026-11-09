# Topic 04 - Modules and Project Basics
from datetime import date, timedelta
# Calculate a membership's renewal and reminder dates.
start_date = date(2026, 11, 9)
expiry_date = start_date + timedelta(days=30)
reminder_date = expiry_date - timedelta(days=3)
print('Start:', start_date)
print('Expires:', expiry_date)
print('Send reminder:', reminder_date)
print('Days active:', (expiry_date - start_date).days)
