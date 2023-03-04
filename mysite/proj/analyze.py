import os
import json
a = os.system('python3 -m pycodestyle views.py > /dev/null 2>&1')
os.system('python3 -m bandit -r views.py -f json -o ./out.json > /dev/null 2>&1')
with open('out.json', 'r') as f:
    b = json.load(f)
if b['results'] or a:
    raise RuntimeError('error!')