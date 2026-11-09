# Topic 06 - Error Handling and Logging
from pathlib import Path
report = Path(__file__).parent / 'output' / 'today.txt'
report.parent.mkdir(exist_ok=True)
try:
    text = report.read_text(encoding='utf-8')
except FileNotFoundError:
    print('Report missing. Creating an empty report.')
    report.write_text('No transactions yet\n', encoding='utf-8')
else:
    print('Existing report:', text.strip())
print('Ready:', report.exists())
