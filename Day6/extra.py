f = open("input.txt").readline()
lastFour = [f[0]]*14

for i, char in enumerate(f, start=1):
    lastFour.append(char)
    lastFour.pop(0)
    if len(set(lastFour)) == 14:
        print(i)
        exit(0)