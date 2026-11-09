# Topic 05 - Files Folders and Data
from pathlib import Path
# Create a realistic folder structure for monthly reports.
root = Path(__file__).parent / 'output' / 'reports'
for month in ['January', 'February', 'March']:
    month_dir = root / month
    month_dir.mkdir(parents=True, exist_ok=True)
    report = month_dir / 'sales.txt'
    report.write_text('Sales report for ' + month, encoding='utf-8')
for report in sorted(root.rglob('*.txt')):
    print('Report:', report.relative_to(root))
