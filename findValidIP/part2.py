def checkIP(entry):
    try:
        parts = entry.split('.')
        return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
    except ValueError:
        return False

mySet = set()

with open('f.inp', 'r') as reader:
    for line in reader:
        currentLine = line.split()
        for word in currentLine: 
            if checkIP(word):
                mySet.add(word)

mySet = sorted(mySet)
print(mySet)
with open('p2output.txt', 'w') as writer:
    for entry in mySet:
        writer.write(entry + '\n')
                