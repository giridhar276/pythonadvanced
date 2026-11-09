# Topic 05 - Files Folders and Data
from pathlib import Path
# Append log messages without replacing older entries.
folder = Path(__file__).parent / 'output'
folder.mkdir(exist_ok=True)
log_file = folder / 'service_log.txt'
log_file.write_text('09:00 - Shop opened\n', encoding='utf-8')
with log_file.open('a', encoding='utf-8') as file:
    file.write('10:30 - First shipment received\n')
    file.write('12:00 - Inventory counted\n')
for line in log_file.read_text(encoding='utf-8').splitlines():
    print(line)
