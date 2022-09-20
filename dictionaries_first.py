name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
count = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        name = words[1]
        count[name] = count.get(name,0) + 1


max_name = None
max_number = None

for key, value in count.items():
    if max_name is None or value > max_number:
        max_name = key
        max_number = value

print(max_name, max_number)
