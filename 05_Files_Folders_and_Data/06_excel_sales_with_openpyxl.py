# Topic 05 - Files Folders and Data
# Requires: pip install openpyxl
from pathlib import Path
from openpyxl import Workbook, load_workbook
path = Path(__file__).parent / 'output' / 'sales.xlsx'
path.parent.mkdir(exist_ok=True)
book = Workbook()
sheet = book.active
sheet.append(['Product', 'Quantity', 'Price'])
sheet.append(['Pen', 5, 20])
sheet.append(['Book', 2, 150])
book.save(path)
data = load_workbook(path, read_only=True).active
for product, quantity, price in list(data.values)[1:]:
    print(product, 'Total:', quantity * price)
