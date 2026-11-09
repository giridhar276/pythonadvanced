# Topic 04 - Modules and Project Basics
# Create a small module beside this script, then import it.
from pathlib import Path
import importlib.util
module_file = Path(__file__).with_name('tax_helper.py')
module_file.write_text('def add_tax(price, rate):\n    return price + price * rate\n')
spec = importlib.util.spec_from_file_location('tax_helper', module_file)
tax_helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tax_helper)
print('Bill with tax:', tax_helper.add_tax(1200, 0.05))
print('Module file:', module_file.name)
