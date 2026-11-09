# Topic 04 - Modules and Project Basics
# main() keeps the program's entry point easy to locate.
def get_inventory():
    return {'Notebook': 12, 'Pen': 30, 'Marker': 8}

def show_low_stock(inventory, limit=15):
    for product, count in inventory.items():
        if count < limit:
            print('Reorder:', product, 'Available:', count)

def main():
    inventory = get_inventory()
    print('Inventory items:', len(inventory))
    show_low_stock(inventory)

if __name__ == '__main__':
    main()
