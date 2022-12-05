# MOVING RETAINS ORDER

f = open("input.txt")
state = 0
stacks = [] # Two dim array
stackLine = 0

def move(arr, n, fr, to):
    for i in range(n-1, -1, -1):
        # print("FUNC: move no", i+1, "from", fr, "to", to)
        # print(arr)
        arr[to-1].append(arr[fr-1][-(i+1)])
        # print(arr)
        arr[fr-1].pop(-(i+1))
        # print(arr)
        # print()
    # print("DONE making move")
    return arr

for line in f.readlines():
    l = line.replace("\n", "")
    if state == 0: # Need to find how many stacks exist
        linelen = len(l)
        crateStacks = (linelen+1) // 4
        print(crateStacks, "stacks")
        state += 1

    if state == 1: # Make arrays
        for i in range(0, crateStacks):
            stacks.append([])
        state += 1

    if state == 2: # Get info from towers
        if l[1] == '1': # End of info
            state += 1
            continue # next line
        else:
            
            # print("Line: '", end="")
            # Go through every stack
            for i in range(0, crateStacks):
                if l[i*4 + 1] != ' ':
                    stacks[i].append(l[i*4 + 1]) # Add to array if there is a crate here
                    print(stacks[i][-1], end="")
            stackLine += 1
            # print("'")
    
    if state == 3: 
        # Reverse stacks
        for i in range(0, crateStacks):
            stacks[i] = stacks[i][::-1]
        
        print(stacks)
        state += 1
    
    if state == 4: 
        # Make moves
        words = l.split(" ")
        # print("LINE", l)
        if words[0] == "move":
            # print("Making move")
            stacks = move(stacks, int(words[1]), int(words[3]), int(words[5]))

print(stacks)
for i in range(0, crateStacks):
    print(stacks[i][-1], end="")
        
