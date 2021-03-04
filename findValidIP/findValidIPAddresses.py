import os
# Finds all distinct IP addresses from all the files in the root directory 
# and print them in lexicographical order.

def checkIP(entry):
    try:
        parts = entry.split('.')
        return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
    except ValueError:
        return False

root = 'input_dir'
mySet = set()

for path, subdirs, files in os.walk(root):
    for name in files:
        # print(os.path.join(path, name))
        with open(os.path.join(path, name), 'r') as reader:
            for line in reader:
                currentLine = line.split()
                for word in currentLine: 
                    if checkIP(word):
                        mySet.add(word)

mySet = sorted(mySet)
print(mySet)
with open('foutput.txt', 'w') as writer:
    for entry in mySet:
        writer.write(entry + '\n')
                