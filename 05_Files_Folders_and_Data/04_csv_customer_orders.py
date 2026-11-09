# Topic 05 - Files Folders and Data
import csv
from pathlib import Path
path = Path(__file__).parent / 'output' / 'orders.csv'
path.parent.mkdir(exist_ok=True)
rows = [{'id': 101, 'customer': 'Asha', 'amount': 850},
        {'id': 102, 'customer': 'Ravi', 'amount': 1200}]
with path.open('w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'customer', 'amount'])
    writer.writeheader()
    writer.writerows(rows)
with path.open(newline='', encoding='utf-8') as file:
    for order in csv.DictReader(file):
        print(order['customer'], 'paid', order['amount'])
