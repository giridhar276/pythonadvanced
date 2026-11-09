# Topic 06 - Error Handling and Logging
import logging
# Logging exception details helps investigate failures.
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')
customer_data = [{'name': 'Asha', 'points': 50},
                 {'name': 'Ravi'}, {'name': 'Meena', 'points': 40}]
for customer in customer_data:
    try:
        points = customer['points']
        print(customer['name'], 'Reward:', points * 2)
    except KeyError:
        logging.exception('Missing points for %s', customer['name'])
