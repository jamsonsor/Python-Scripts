def checkIP(entry):
    try:
        parts = entry.split('.')
        return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
    except ValueError:
        return False

with open('file1.txt', 'r') as reader:
    for line in reader:
        currentLine = line.split()
        for word in currentLine: 
            if checkIP(word):
                print(word)

                