# Topic 05 - Files Folders and Data
from pathlib import Path
# Write and read a shift handover note.
folder = Path(__file__).parent / 'output'
folder.mkdir(exist_ok=True)
file = folder / 'handover.txt'
file.write_text('Pending orders: 4\nDamaged boxes: 1\n', encoding='utf-8')
print('Saved:', file.name)
print('Handover details:')
print(file.read_text(encoding='utf-8'))
