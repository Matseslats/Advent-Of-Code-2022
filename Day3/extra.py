f = open("input.txt")

matchChars = 0

def val(c):
    asciiVal = ord(c)
    if 97 <= asciiVal <= 122: # Lowercase
        intVal = asciiVal -96
    if 65 <= asciiVal <= 90: # Uppercase
        intVal = asciiVal - 65+27
    return intVal

def getLine():
    line =  f.readline().replace('\n', '')
    return line


while True:
    firstThird = getLine()
    secondThird = getLine()
    thirdThird = getLine()
    if firstThird == "" or secondThird == "" or thirdThird == "": # Not enough to continue
        print(matchChars)
        exit(0)

    # Check for new matches
    matchThis = []
    for i in firstThird:
        for j in secondThird:
            for k in thirdThird:
                if i == j == k and not i in matchThis:
                    matchThis.append(i)
                    break
    
    # Add sum
    for char in matchThis:
        matchChars += val(char)

    