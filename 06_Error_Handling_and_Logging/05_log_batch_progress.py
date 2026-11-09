# Topic 06 - Error Handling and Logging
import logging
from pathlib import Path
folder = Path(__file__).parent / 'output'
folder.mkdir(exist_ok=True)
logging.basicConfig(filename=folder / 'batch.log', level=logging.INFO,
                    format='%(levelname)s - %(message)s', force=True)
orders = {'ORD1': 250, 'ORD2': 0, 'ORD3': 700}
for order_id, amount in orders.items():
    if amount <= 0:
        logging.warning('Skipped invalid order %s', order_id)
        continue
    logging.info('Processed %s for %s', order_id, amount)
    print('Processed:', order_id)
print('Log saved to:', folder / 'batch.log')
