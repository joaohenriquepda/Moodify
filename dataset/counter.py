import json
import sys

file_path = sys.argv[1] 

with open(file_path, 'r') as f:
    data = json.load(f)

print(len(data))