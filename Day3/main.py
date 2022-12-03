f = open("input.txt")
lines = f.readlines()

matchChars = 0

def val(c):
    asciiVal = ord(c)
    if 97 <= asciiVal <= 122: # Lowercase
        intVal = asciiVal -96
    if 65 <= asciiVal <= 90: # Uppercase
        intVal = asciiVal - 65+27
    return intVal

# Loop through lines
for line in lines:
    line.replace("\n", "")
    lineLen = len(line)

    # Split line in half
    firstHalf = line[:lineLen//2] # // Integer division
    secondHalf = line[lineLen//2:]

    # Check for new matches
    matchThis = []
    for i in firstHalf:
        for j in secondHalf:
            if i == j and not i in matchThis:
                matchThis.append(i)
                break
    
    # Add sum
    for char in matchThis:
        matchChars += val(char)

print(matchChars)
    