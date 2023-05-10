import pandas as pd
import json

df = pd.DataFrame(columns=['checker', 'location', 'severity'])
df = df.append({'checker': 'chk1', 'location': 'somewhere', 'severity': 
'high'}, ignore_index=True)

with open('results.json') as f:
    file = json.load(f)

issues_list = file['issues']['issues']

for issue in issues_list:
    row_entry = {'checker': issue['checker_id'], 'location': 
f"{issue['filepath']}:{issue['location']['start']['line']}", 'severity': 
issue['severity']['impact']}
    print(row_entry)
    df = df.append(row_entry, ignore_index=True)

df.to_csv('results.csv')
