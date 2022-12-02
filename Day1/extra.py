response = open("input.txt")
lines = response.readlines()

currentMax = { 
    0: 0, # Most
    1: 0, # 2nd Most
    2: 0 # 3rd most
}

currentCount = 0
for line in lines:
    try:
        currentCount += int(line)
    except:
        if currentCount >= currentMax[0]:
            currentMax[2], currentMax[1], currentMax[0] = currentMax[1], currentMax[0], currentCount     
        elif currentCount >= currentMax[1]:
            currentMax[2], currentMax[1] = currentMax[1], currentCount     
        elif currentCount >= currentMax[2]:
            currentMax[2] = currentCount
            
        currentCount = 0

print(currentMax[0]+currentMax[1]+currentMax[2])