# Topic 05 - Files Folders and Data
import json
from pathlib import Path
products = [{'name': 'Laptop', 'price': 45000},
            {'name': 'Mouse', 'price': 550}]
path = Path(__file__).parent / 'output' / 'products.json'
path.parent.mkdir(exist_ok=True)
path.write_text(json.dumps(products, indent=2), encoding='utf-8')
saved_products = json.loads(path.read_text(encoding='utf-8'))
for product in saved_products:
    print(product['name'], 'price:', product['price'])
