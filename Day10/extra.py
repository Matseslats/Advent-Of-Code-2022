f = open("input.txt")
sum = 0
cycle = 0 # pixed being drawn
offset = 0
x = 1

def checkClock():
    global sum, offset
    spriteVis = (x+2 >= (cycle+offset) >= x)
    
    if spriteVis: # Draw pixel
        print("#", end="")
    else:
        print(".", end="")

    if cycle % 40 == 0: # New line
        offset -= 40
        print()


for line in f.readlines():
    l = line.replace("\n", "")
    if l == "noop": # No operation
        cycle += 1
        checkClock()
    instrs = l.split(" ")
    if instrs[0] == "addx": # Takes two clock cycles before x is incremented
        cycle += 1
        checkClock()
        cycle += 1
        checkClock()
        x += int(instrs[1])

print(sum)