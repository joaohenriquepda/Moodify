import json
import sys

file_path = sys.argv[1] 
new_file = sys.argv[2]

with open(file_path, 'r') as f:
    data = json.load(f)

elements = []

for element in data:
    elements.append(element[0])

with open(new_file, 'w') as f:
    json.dump(elements, f, indent=2)
    print('FINISH')

#print(json.dumps(element, sort_keys=True, indent=4))


# for element in elements:
#     print(json.dumps(element, sort_keys=True, indent=4))

    

# print(json.dumps(elements, sort_keys=True, indent=4))

# with open(new_file, 'w') as f:
#     json.dump(data, f, indent=2)
#     print('FINISH')