import json
import sys

file_path = sys.argv[1] 
new_file = sys.argv[2]

with open(file_path, 'r') as f:
    data = json.load(f)

for element in data:
    if type(element) is dict:
        del element["type"]
        del element['analysis_url']
        del element['duration_ms']
        del element['track_href']
        del element['uri']

with open(new_file, 'w') as f:
    json.dump(data, f, indent=2)
    print('FINISH')