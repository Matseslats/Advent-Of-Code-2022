response = open("input.txt")
lines = response.readlines()

currentMax = 0
currentCount = 0
for line in lines:
    try:
        currentCount += int(line)
    except:
        currentMax = max(currentCount, currentMax)
        currentCount = 0

print(currentMax)